"""Time sleep
Number of seconds you want the program to stay paused.
Ctrl-C to stop the program raise an exception.
"""
import time, sys

def tick_tack():
    print('Tick'), time.sleep(1)
    print('Tock'), time.sleep(1)

while(True):
    try:
        tick_tack()
    except KeyboardInterrupt:
        sys.exit()

    # Tick
    # Tock
    # Tick
    # Tock
    # Tick
    # Tock