# Factorial definition: 
# 
# 0! is 1
# n! = n(n-1)!
#
# 3! is 3 times 2!, which is 2 times 1!, which is 1 times 0!.
# 3! = 3 * 2! = 3 * 2 * 1! = 3 * 2 * 1 * 0! = 6

def factorial(n):
    
    if (n == 0): return 1

    n = n * factorial(n-1)
    return n

assert factorial(3) == 6
assert factorial(0) == 1
assert factorial(4) == 24
assert factorial(9) == 362880  # tic-tac-toe combinations