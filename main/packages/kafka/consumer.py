from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('HelloWorldTopic', bootstrap_servers='localhost: 9092')

for message in consumer:
    print('Received =', message.value.decode())