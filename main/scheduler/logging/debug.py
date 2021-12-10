"""Debug
If you use print() calls to debug your code, 
you'll spend a lot of time to remove thems, once you are done.
With logging module you can easily switch between ...
showing or hidding messages.
"""
import logging
logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def factorial(n):
    if (n < 0):
        logging.critical('n is not positive!')
        return None
    if (n == 0): return 1
    n = n * factorial(n-1)
    logging.debug('n is ' + str(n))
    return n


"""Logging messages enabled:
"""
assert factorial(-1) == None
assert factorial(4)  == 24
    # 2021-12-10 16:31:44,977 - CRITICAL - n is not positive!
    # 2021-12-10 16:18:59,379 - DEBUG - n is 1
    # 2021-12-10 16:18:59,379 - DEBUG - n is 2
    # 2021-12-10 16:18:59,379 - DEBUG - n is 6
    # 2021-12-10 16:18:59,379 - DEBUG - n is 24


"""Disable logging messages:
Only level > ERROR messages are displayed
"""
logging.disable(logging.ERROR)
assert factorial(-1) == None
assert factorial(0)  == 1
assert factorial(3)  == 6
assert factorial(4)  == 24
    # 2021-12-10 16:34:58,048 - CRITICAL - n is not positive!