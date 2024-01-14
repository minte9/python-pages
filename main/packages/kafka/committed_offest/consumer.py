from kafka import KafkaConsumer, TopicPartition
import time
import sys
import re

consumer = KafkaConsumer(bootstrap_servers='localhost: 9092', group_id='my-group')
partition = TopicPartition('AccessLogTopic', 0)
consumer.assign([partition])

# Retrieve the current committed offset for partition
committed_offset = consumer.committed(partition)

try:
    for message in consumer:
        received_message = message.value.decode()

        # Extract the IP and path from the message
        pattern = r'(\d{1,3}(?:\.\d{1,3}){3}) - - \[(.*) \+0200\] "GET (/.+?) HTTP/'
        match = re.search(pattern, received_message)

        if match:
            ip = match.group(1)
            time = match.group(2)
            path = match.group(3)
            print(f"Received: {time} {ip} {path}")

        # Commit the offset after processing the message
        consumer.commit()

except KeyboardInterrupt:
    print("Interrupted by user")
    sys.exit(0)
finally:
    consumer.close()


"""
    Received: 2023-11-17 16:28:46 /usr/bin/pip list
    Received: 2023-11-17 16:29:19 /usr/bin/apt list --upgradable
"""