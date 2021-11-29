"""With open statement benefits:
Open multiple files in a single with statement.
"""

import os

DIR = os.path.dirname(os.path.realpath(__file__))
A = DIR + "/data/A.txt"
B = DIR + "/data/B.txt"

with open(A, "w") as fa, open(B, "w") as fb:
    fa.write(os.path.basename(A) + ": Line 1")
    fb.write(os.path.basename(B) + ": Line 1")

with open(A) as fa, open(B) as fb:
    print(fa.read()) # myfileA.txt: Line 1
    print(fb.read()) # myfileB.txt: Line 1