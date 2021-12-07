#!python3
"""Multi-clipboard application.
This program saves every clipboard text under a key.
The .pyw extension means that Python won't open a terminal.
python multi_clipboard.pyw
"""
import shelve, pyperclip, sys, os
DIR = os.path.dirname(os.path.realpath(__file__))
FILE = DIR + "/data/clipboard.shelve"

with shelve.open(FILE) as db:

    dict = db['keywords'] if 'keywords' in db.keys() else {}

    action  = sys.argv[1] if len(sys.argv) == 3 else ''
    keyword = sys.argv[2] if len(sys.argv) == 3 else ''

    if action.lower() == 'load':
        text = dict[sys.argv[2]]
        pyperclip.copy(text)
        print("Text in clipboard: " + text)

    if action.lower() == 'save':
        keyword = sys.argv[2]
        dict[keyword] = pyperclip.paste()

    db['keywords'] = dict
    print(db['keywords'])


# ./multi_clipboard.pyw
# {}
#
# Copy text: AAA
# ./multi_clipboard.pyw save a
# {'a': 'AAA'}
#
# Copy text: BBB
# ./multi_clipboard.pyw save b
# {'a': 'AAA', 'b': 'BBB'}
#
# ./multi_clipboard.pyw load a
# Text in clipboard: AAA