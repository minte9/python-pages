"""Logging
Set basic configuration to add logging to your program.
Factorial: n! = n(n-1)!
"""
import logging
logging.basicConfig(level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def factorial(n):
    if (n == 0): return 1
    logging.debug('factorial(%s)' % n)
    n = n * factorial(n-1)
    logging.debug('n is ' + str(n))
    return n

factorial(4)

"""
2021-12-10 16:04:03,046 - DEBUG - factorial(4)
2021-12-10 16:04:03,046 - DEBUG - factorial(3)
2021-12-10 16:04:03,047 - DEBUG - factorial(2)
2021-12-10 16:04:03,047 - DEBUG - factorial(1)
2021-12-10 16:04:03,047 - DEBUG - n is 1
2021-12-10 16:04:03,047 - DEBUG - n is 2
2021-12-10 16:04:03,047 - DEBUG - n is 6
2021-12-10 16:04:03,047 - DEBUG - n is 24
"""