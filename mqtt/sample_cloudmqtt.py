# Inspired and modified from https://github.com/CloudMQTT/python-mqtt-example
import os
import configparser
from urllib.parse import urlparse
import paho.mqtt.client as mqtt

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

client = mqtt.Client()
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#client.on_log = on_log

# Get CLOUDMQTT settings from config.ini 
CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
CONFIG_MQTT = CONFIG['Cloudmqtt']
TOPIC = CONFIG_MQTT['TOPIC']
FIRST_MESSAGE = CONFIG_MQTT['MESSAGE']


# Connect
client.username_pw_set(CONFIG_MQTT['USER'], CONFIG_MQTT['PASSWORD'])
client.connect(CONFIG_MQTT['CLOUDMQTT_URL'], int(CONFIG_MQTT['PORT']))

# Start subscribe, with QoS level 0
client.subscribe(TOPIC, 0)

# Publish a message
client.publish(TOPIC, FIRST_MESSAGE)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = client.loop()
print("rc: " + str(rc))