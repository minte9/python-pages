import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')

    def on_modified(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

"""
    event type: created  path : ./watchdog/file.txt
    event type: modified  path : ./watchdog
"""