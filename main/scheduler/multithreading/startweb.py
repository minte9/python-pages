"""
Start server / Open URL
Run from console / python startweb.py 
Interrupt / Ctrl + C to kill process
"""
import sys, time, threading, webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

def start_server():
    httpd = HTTPServer(('127.0.0.1', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()

threading.Thread(target=start_server).start()
webbrowser.open_new('http://127.0.0.1:8000/')

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)