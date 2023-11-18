from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('ApiDataTopic', bootstrap_servers='localhost:9092')
CODE = 'EUR'

for message in consumer:
    received_message = json.loads(message.value.decode())

    name = received_message['chartName']
    updated = received_message['time']['updated']
    rate = received_message['bpi'][CODE]['rate']

    print(f"{name} {rate} {CODE} {updated}")

"""
    Bitcoin 35,718.9143 EUR Nov 18, 2023 17:36:00 UTC
    Bitcoin 35,718.9143 EUR Nov 18, 2023 17:36:00 UTC
    Bitcoin 35,720.2254 EUR Nov 18, 2023 17:37:00 UTC
    Bitcoin 35,720.2254 EUR Nov 18, 2023 17:37:00 UTC
    Bitcoin 35,733.4247 EUR Nov 18, 2023 17:38:00 UTC
    ...
"""