from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Open the file in read mode
with open('/var/log/auth.log', 'r') as file:

    # Move the cursor to the end of the file (offset=0, whence=2)
    file.seek(0, 2)

    while True:
        line = file.readline()

        if line:
            producer.send('LogFileTopic', value=line.encode())
            producer.flush()
            print('Produced:', line.strip())

        time.sleep(1)

"""
    Produced: Nov 17 16:28:46 i15pc3 sudo:  catalin : TTY=pts/19 ; PWD=/ ; USER=root ; COMMAND=/usr/bin/pip list
    Produced: Nov 17 16:28:46 i15pc3 sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
    Produced: Nov 17 16:28:47 i15pc3 sudo: pam_unix(sudo:session): session closed for user root

    Produced: Nov 17 16:29:18 i15pc3 sudo:  catalin : TTY=pts/19 ; PWD=/ ; USER=root ; COMMAND=/usr/bin/apt list --upgradable
    Produced: Nov 17 16:29:04 i15pc3 sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
    Produced: Nov 17 16:29:04 i15pc3 sudo: pam_unix(sudo:session): session closed for user root
"""
