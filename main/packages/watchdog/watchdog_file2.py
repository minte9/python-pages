"""
    Watchdog provides an efficient way to monitor file changes. 
    It can notify your application immediately when a new line is added to the log file. 
    This is more efficient than continuously polling the file for changes, 
    which can use unnecessary CPU and I/O resources.
"""
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

# FILE = "/var/log/auth.log"
# FILE = "/var/log/apache2/refresh.local-access.log"

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