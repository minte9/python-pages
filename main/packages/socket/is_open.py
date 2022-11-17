"""Using Python to check if remote port is open and accessible
"""
import socket

def is_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print("open")
        else:
            print("not open")

is_open('python.org', 80)
is_open('python.org', 8080)