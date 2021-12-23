"""Import module:
Any file that contains Python code can be imported as module.
Test code (defined in mymodule) is not displayed.
"""
from mymodule import mysum as sum
from mymodule import myprint as print

print('Hello World')
    # Print from my module: Hello World: __main__

print(sum(1,2))
    # Print from my module: 3