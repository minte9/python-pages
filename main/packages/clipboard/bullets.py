"""Add bullets to a list
The tranformed list will be automatically ...
available in the clipboard.
Copy:
    Name: pyperclip
    Version: 1.8.2
    Author: Al Sweigart
    License: BSD
Run:
    $ python bullets.py
Paste:
    * Name: pyperclip
    * Version: 1.8.2
    * Author: Al Sweigart
    * License: BSD
"""
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
lines = [f'* {k}' for k in lines]
text = '\n'.join(lines)

pyperclip.copy(text) # text ready to be paste