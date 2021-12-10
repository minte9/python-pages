"""Open subprocess:
If you open for example calculator program multiple times, 
each window is a different process of the application.

Every process can have multiple threads.
Unlike threads, a process cannot read and write another process's variable.
It's like having a separate copy of the program code.
"""
import subprocess

subprocess.Popen('/usr/bin/gnome-calculator')
subprocess.Popen('/usr/bin/gnome-calculator')

# Opens calculator twice