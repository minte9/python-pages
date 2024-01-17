from kafka import KafkaProducer
import time
import sys
import re
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def process_message(line):
    """
        Sample log line:
        "127.0.0.1 - - [17/Jan/2024:19:45:39 +0200] \"GET /algorithms/
        HTTP/1.1\" 200 13275 \"http://refresh.local/algorithms\" \"Mozilla/5.0 (X11; 
        Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36\""
    """
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
    match = re.match(pattern, line)
    if match:
        log_data = {
            "ip_address": match.group(1),
            "datetime": match.group(2),
            "request": match.group(3),
            "status_code": int(match.group(4)),
            "response_size": int(match.group(5)),
            "referer": match.group(6),
            "user_agent": match.group(7)
        }
        # Convert to JSON
        json_data = json.dumps(log_data)
    else:
        json_data = {}
    return json_data

# Open the file in read mode
with open('/var/log/apache2/refresh.local-access.log', 'r') as file:
    file.seek(0, 2) # end of the file
    
    try:
        while True:
            line = file.readline()
            if line:
                message = process_message(line)
                producer.send('AccessLogTopic', message.encode())
                producer.flush()
                print('AccessLog:', message.strip())
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
