"""A program that can be run with command line arguments
(a short keyphrase like: agree or busy)
This way the user can have long related text in clipboard,
without having to retype all text.
Usage: python multiclipboard.py [keyphrase]
"""
import sys, pyperclip

TEXT = {
    'agree': """I agree, that sounds fine to me.""",
    'busy': """Sorry, I am not available right now.""",
}

if len(sys.argv) < 2:
    print('Correct usage: py multiclipboard.py [keyphrase]')
    print('To copy phrase text in the clipboard')
    sys.exit()

key = sys.argv[1]

if key not in TEXT:
    print(f'There is no text for [{key}]')
    sys.exit()

pyperclip.copy(TEXT[key])
print(f'Text for [{key}] copied to clipboard.') # Look Here

"""
$ python multiclipboard.py something
    # There is no text for [text]

$ python multiclipboard.py agree
    # Text for [agree] copied to clipboard.

$ Ctrl + Shift + V
    # I agree, that sounds fine to me.
"""