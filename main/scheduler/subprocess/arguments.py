"""Open subprocess arguments:
Most GUI applications will accept a single argument for a file to be open.
You pass a list as sole argument to Popen()

Each operating system has a program that is equivalent to double-click
Windows: start / Linux: see

The wait() method will block until the launched process has terminated.
This is useful to let the user finish with other programs.
"""
import subprocess, pathlib, sys

DIR = pathlib.Path(__file__).resolve().parent
A = subprocess.Popen(['/usr/bin/gedit', DIR/'files/A.txt'])
A.wait()

with open(DIR / 'files/B.txt', 'w') as f:
    f.write('Hello World!')
B = subprocess.Popen(['/usr/bin/see', DIR / 'files/B.txt'])
B.wait()