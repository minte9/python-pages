# ------------------------------
# FIBONACCI - DICTIONARY version
# ------------------------------ 
# Keep track of values and store them in a dictionary. 
# This is called memoization.
# The algorithm is O(n).
#
#    fb(0) = 0
#    fb(1) = 1
#    fb(n) = fb(n-1) + fb(n-2)
#
# Fibonacci is naturally iterative.

def fibonacci(n):
    known = {0:0, 1:1}
    
    for i in range(2, n + 1):
        known[i] = known[i -1] + known[i -2]

    return known[n]


assert fibonacci(4) == 3  # 9
assert fibonacci(5) == 5  # 24
assert fibonacci(6) == 8  # 49

fibonacci(1000)  # works