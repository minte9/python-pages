"""Using Python to check if remote port is open and accessible
connect_ex() return an error indicator ...
instead of raising an exception
"""
import socket

def is_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        res = s.connect_ex((host, port))
        if res == 0:
            print("open")
        else:
            print("not open")

is_open('python.org', 80)
is_open('python.org', 8080)