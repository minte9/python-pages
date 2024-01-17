from kafka import KafkaProducer
import time
import sys

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Open the file in read mode
with open('/var/log/apache2/refresh.local-access.log', 'r') as file:
    file.seek(0, 2) # end of the file
    
    try:
        while True:
            line = file.readline()
            if line:
                message = process_message(line)
                producer.send('AccessLogTopic', value=line.encode())
                producer.flush()
                print('AccessLog:', line.strip())
            time.sleep(1)
    except KeyboardInterrupt:
        print("Interrupted by user")
        sys.exit(0)
    finally:
        producer.close()

"""
    AccessLog: 127.0.0.1 - - [14/Jan/2024:11:26:50 +0200] "GET /algorithms HTTP/1.1" 200 5594 ...
    AccessLog: 127.0.0.1 - - [14/Jan/2024:12:02:22 +0200] "GET /spring-boot HTTP/1.1" 200 5090 ...
"""
