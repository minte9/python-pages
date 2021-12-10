"""Threads Concurency:
When you create a new thread make sure its target function
uses only local variable in that function.
"""
import threading, time


"""Incorrect"""
i = 0
def pause():
    global i # Look Here
    while i < 3:
        print('Run thread: ' + threading.currentThread().name)
        i = i + 1
        time.sleep(1)

print('Start')
threading.Thread(target=pause, name='A').start()
threading.Thread(target=pause, name='B').start()
print('End')
    # Start
    # Run thread: A
    # Run thread: B
    # End
    # Run thread: A

time.sleep(3)
print()


"""Correct"""
def pauseC():
    i = 0 # Look Here
    while i < 3:
        print('Run thread: ' + threading.currentThread().name)
        i = i + 1
        time.sleep(1)

print('Start')
threading.Thread(target=pauseC, name='A2').start()
threading.Thread(target=pauseC, name='B2').start()
print('End')
    # Start
    # Run thread: A2
    # Run thread: B2
    # End
    # Run thread: A2
    # Run thread: B2
    # Run thread: A2
    # Run thread: B2