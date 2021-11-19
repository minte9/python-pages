# Pipe object:
#
# Programs launched from the shell ...
# can also be launch from Python using pipe object.
#
# The return value is an object that behaves like a file.

import os

cmd = 'ls -l'
fp = os.popen(cmd)
res = fp.read()
print(res)
    # -rw-rw-r-- 1 catalin catalin 16384 iul 15 12:35 images_db
    # drwxr-xr-x 3 catalin catalin  4096 iul 13 09:35 layouts
    # drwxr-xr-x 5 catalin catalin  4096 iun  4  2020 library

stat = fp.close()
print(stat) # None (no errors)