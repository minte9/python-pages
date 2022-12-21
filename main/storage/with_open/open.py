"""With open statement benefits:
No need to close the file, 'with open' takes care of that.
Fewer lines of code,fewer bugs."""

import os

DIR = os.path.dirname(os.path.realpath(__file__))
file = DIR + "/data/file.txt"

with open(file, "w") as f:
    f.write("New line 1 \n")
    f.write("New line 2 \n")

with open(file) as f:
    print(f.read())
        # New line 1
        # New line 2 