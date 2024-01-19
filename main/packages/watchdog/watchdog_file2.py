from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class MyHandler(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename
        self.last_known_size = os.path.getsize(filename)

    def on_modified(self, event):
        if event.src_path == self.filename:
            new_size = os.path.getsize(self.filename)
            if new_size > self.last_known_size:
                with open(self.filename, 'r') as f:
                    f.seek(self.last_known_size)
                    print(f.read().strip())
                self.last_known_size = new_size

DIR = os.path.dirname(os.path.realpath(__file__))
FILE = DIR + "/file.txt"

event_handler = MyHandler(FILE)
observer = Observer()
observer.schedule(event_handler, path=FILE, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

"""
    write 1
    write 2
"""