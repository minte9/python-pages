# Slow - only recursion
#
#    fb(0) = 0
#    fb(1) = 1
#    fb(n) = fb(n-1) + fb(n-2)
#
# Each number is the sum of the two preceding ones.
#
# The bigger the argument, the longer the function runs.
# It gets worst as the argument gets bigger.

loops = 0
def fibonacci(n):

    global loops
    loops = loops + 1

    if n == 0: return 0
    if n == 1: return 1

    return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(4) == 3;           print (loops) # 9
assert fibonacci(5) == 5;           print (loops) # 24
assert fibonacci(6) == 8;           print (loops) # 49

fibonacci(30)
print (loops) # 2692537 - Look Here