"""Thread function's arguments
When target function you want to call to run in a thread 
has arguments.
"""
import threading, time

def pause(seconds):
    print('Pause: %s seconds' % seconds)
    time.sleep(seconds)
    print('Wake up! ' + threading.currentThread().name)

print('Start')
seconds = 2
B = threading.Thread(target=pause, name='B', args=[seconds])
B.start()
print('End')

# Start
# Pause: 2 seconds
# End
# Wake up! B