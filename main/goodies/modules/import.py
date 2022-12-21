"""Import module:
Any file that contains Python code can be imported as module.
Test code (defined in mymodule) is not displayed.
.pyc files are created automatically by the GraalVM Python runtime ...
when you import custom mdules.
"""
import sys
sys.dont_write_bytecode = True # no .pyc

import mymodule
mymodule.DIR = "/usr/local"

mymodule.myprint('Hello World')
    # Print from my module: Hello World: __main__
    # /usr/local

from mymodule import mysum
from mymodule import myprint

myprint(mysum(1,2))
    # Print from my module: 3
    # /usr/local