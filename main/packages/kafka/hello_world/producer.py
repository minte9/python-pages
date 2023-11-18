from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    message = "Hello, Kafka!"
    producer.send('HelloWorldTopic', value=message.encode())
    producer.flush()

    print("Produced =", message)
    time.sleep(1)

"""
    Produced = Hello, Kafka!
    Produced = Hello, Kafka!
    Produced = Hello, Kafka!
    ...
"""