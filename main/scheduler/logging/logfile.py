"""Logging messages to file:
Screen messages are helpful, but they can make the output ...
hard to read.
Writting logging messages to a file keeps your screen clean.
"""
import logging, pathlib
DIR = pathlib.Path(__file__).resolve().parent

logging.basicConfig(
    level=logging.DEBUG, 
    filename=DIR/'logs/file1.log', 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def factorial(n):
    if (n < 0):
        logging.critical(f'Number {n} is not positive!')
        return None
    if (n == 0): return 1
    n = n * factorial(n-1)
    logging.debug('n is ' + str(n))
    return n

assert factorial(-1)  == None
assert factorial(4)   == 24
assert factorial(-11) == None


""" logs/file1.log
--------------------------------------------------------------
2021-12-10 17:09:40,229 - CRITICAL - Number -1 is not positive!
2021-12-10 17:09:40,229 - DEBUG - n is 1
2021-12-10 17:09:40,229 - DEBUG - n is 2
2021-12-10 17:09:40,229 - DEBUG - n is 6
2021-12-10 17:09:40,229 - DEBUG - n is 24
2021-12-10 17:09:40,229 - CRITICAL - Number -11 is not positive!
2021-12-10 17:09:59,231 - CRITICAL - Number -1 is not positive!
2021-12-10 17:09:59,231 - DEBUG - n is 1
2021-12-10 17:09:59,231 - DEBUG - n is 2
2021-12-10 17:09:59,231 - DEBUG - n is 6
2021-12-10 17:09:59,232 - DEBUG - n is 24
2021-12-10 17:09:59,232 - CRITICAL - Number -11 is not positive!
"""