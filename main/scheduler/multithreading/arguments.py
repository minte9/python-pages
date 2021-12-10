"""Thread function's arguments
When target function you want to call to run in a thread 
has arguments.
"""
import threading, time

def pause(seconds):
    i = 0
    while i < seconds:
        print('Run thread: ' + threading.currentThread().name)
        i = i + 1
        time.sleep(1)

print('Start main')
threading.Thread(target=pause, name='B', args=[5]).start()
print('End main')

# Start main
# Run thread: B
# End main
# Run thread: B
# Run thread: B
# Run thread: B
# Run thread: B