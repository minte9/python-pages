"""Find all authors @nickname in an amazon page.
Page example: https://www.amazon.com/gp/product/1593279922
Run program: Ctrl-A, Ctrl-C, run program, Ctrl-V
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