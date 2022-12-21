"""Using Python to check if remote port is open and accessible
connect_ex() return an error indicator ...
instead of raising an exception
"""
import socket

def is_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    res = s.connect_ex((host, port))
    if res == 0:
        print("%s %s open" % (host, port))
    else:
        print("%s %s closed" % (host, port))

is_open('python.org', 80)
is_open('python.org', 8080)

host = input('Host: ') # localhost
port = input('Port: ') # 80
is_open(host, int(port))