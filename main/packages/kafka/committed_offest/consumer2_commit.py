from kafka import KafkaConsumer, TopicPartition
import time
import sys
import re

consumer = KafkaConsumer(bootstrap_servers='localhost: 9092', group_id='my-group')
partition = TopicPartition('AccessLogTopic', 0)
consumer.assign([partition])

# Retrieve the current committed offset for partition
committed_offset = consumer.committed(partition)

for message in consumer:
    received_message = message.value.decode()

    # Extract the IP and path from the message
    pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) - - \[(.*) \+0200\] "GET (/.+?) HTTP/'
    match = re.search(pattern, received_message)

    if match:
        ip = match.group(1)
        time = match.group(2)
        path = match.group(3)
        print(f"Consumer2: {path} {ip} {time}")

    # Commit the offset after processing the message
    consumer.commit()

"""
    Received: 14/Jan/2024:12:05:32 127.0.0.1 /algorithms
    Received: 14/Jan/2024:12:05:33 127.0.0.1 /spring-boot
"""