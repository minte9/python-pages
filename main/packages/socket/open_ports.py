"""Create instance of socket for every port
"""
import socket, threading

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            res = s.connect(("127.0.0.1", port))
            print('Port %s is open' % port)
        except ConnectionRefusedError:
            pass

for i in range(10, 100):
    thread = threading.Thread(target=scan_port, args=[i])
    thread.start()

#Port 21 is open
#Port 25 is open
#Port 80 is open