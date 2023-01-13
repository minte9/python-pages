from asyncio import subprocess
import time, sys
from subprocess import Popen
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import pathlib

DIR = pathlib.Path(__file__).resolve().parent
DIR = str(DIR).replace('python-pages/main/packages/watchdog', '')
DIR_TO_WATCH = DIR + 'python-pages/main/'

class ScriptTriggerHandler(FileSystemEventHandler):

    def on_modified(self, event):
        Popen(['git', 'add ' + DIR_TO_WATCH])
        Popen(['git', 'exportmdfcurl'])
        print('File was modified')

    def on_created(self, event):
        Popen(['git', 'add ' + DIR_TO_WATCH])
        Popen(['git', 'exportmdfcurl'])
        print('File or directory was created')

event_handler = ScriptTriggerHandler()
observer = Observer()
observer.schedule(event_handler, DIR_TO_WATCH, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

