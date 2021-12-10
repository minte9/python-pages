"""Threads:
When you use time.sleep() your program cannot do anything else,
unless you use threads.
A single-thread program is like placing one finger on a line of code,
then moving to the next.
A multi-threaded program has multiple "fingers"
"""
import threading, time

def pause():
    time.sleep(5)
    print('Wake up! ' + threading.currentThread().name)

print('Program start') # main

A = threading.Thread(target=pause) # second
A.start()
B = threading.Thread(target=pause, name='B') # third
B.start()

print('Program end') # main

# Program start
# Program end
# Wake up! Thread-1
# Wake up! B