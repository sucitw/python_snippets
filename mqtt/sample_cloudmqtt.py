# inspired and modified from https://github.com/CloudMQTT/python-mqtt-example
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
config = configparser.ConfigParser()
config.read('config.ini')

config_mqtt = config['Cloudmqtt']
topic = config_mqtt['TOPIC']

# Connect
client.username_pw_set(config_mqtt['USER'], config_mqtt['PASSWORD'])
client.connect(config_mqtt['CLOUDMQTT_URL'], int(config_mqtt['PORT']))

# Start subscribe, with QoS level 0
client.subscribe(topic, 0)

# Publish a message
client.publish(topic, "my message")

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = client.loop()
print("rc: " + str(rc))
