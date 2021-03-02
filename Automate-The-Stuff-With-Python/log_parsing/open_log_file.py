"""
open log file and print it
"""
import os

log_file_path = os.path.normpath(os.path.join(os.getcwd(), "access_log"))

with open(log_file_path, "r") as f:
    for line in f:
        print(line)