from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('ApiDataTopic', bootstrap_servers='localhost:9092')
CODE = 'USD'

for message in consumer:
    received_message = json.loads(message.value.decode())

    name = received_message['chartName']
    updated = received_message['time']['updated']
    rate = received_message['bpi'][CODE]['rate']

    print(f"{name} {rate} {CODE} {updated}")