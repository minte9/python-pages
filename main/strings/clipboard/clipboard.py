"""A program which uses the computer's clipboard,
using pyperclip package, by Al Sweigart
Pyperclip is not part of the standard distribution.
pip install pyperclip
"""
import pyperclip, time

pyperclip.copy('Hello, world!')
clipboard = pyperclip.paste()
print(clipboard)
    # Hello, world!

while(True):
    clipboard = pyperclip.paste() # Look Here
    print(clipboard)
    time.sleep(5)

    # Hello, world!
    # Hello, world!
    # Hello, world!
    # ...
    # copy another text on computer
    # example: a path from terminal
    # ---
    # /usr/bin/python3
    # /usr/bin/python3
    # /usr/bin/python3