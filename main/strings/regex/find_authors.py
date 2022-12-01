"""Find all authors @nickname in an amazon page

Example:
1) Open https://www.amazon.com/gp/product/1593279922
2) Copy Ctrl-A, Ctrl-C
3) Run python program
4) Paste Ctrl-v
"""

import re, pyperclip

clipboard = pyperclip.paste()

pattern = re.compile('@[a-zA-Z0-9_-]+')
authors = pattern.findall(clipboard)

pyperclip.copy('\n'.join(authors))
print(pyperclip.paste())
    # @OscarBaruffa
    # @Awful_Curious
    # @mcapablanca