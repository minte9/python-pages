from kafka import KafkaConsumer
import re
import time

consumer = KafkaConsumer('LogFileTopic', bootstrap_servers='localhost: 9092')

for message in consumer:
    received_message = message.value.decode()

    # Extract command messages
    if 'COMMAND' in received_message:
        match = re.search(r'COMMAND=(.*)', received_message)

        if match:
            command = match.group(1).strip()
            print('Received:', time.strftime("%Y-%m-%d %H:%M:%S") + command)


"""
    Received: 2023-11-17 16:28:46 /usr/bin/pip list
    Received: 2023-11-17 16:29:19 /usr/bin/apt list --upgradable
"""