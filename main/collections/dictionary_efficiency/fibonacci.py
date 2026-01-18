# -------------------------------------
# FIBONACCI - SLOW version
# -------------------------------------
# We use recursion to get the Fibonacci sequence.
# The bigger the argument, the longer the function runs.
#
#    fb(0) = 0
#    fb(1) = 1
#    fb(n) = fb(n-1) + fb(n-2)

loops = 0
def fibonacci(n):
    global loops

    loops = loops + 1

    if n == 0: return 0
    if n == 1: return 1

    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(30)
print ("Loops:", loops)  # Loops: 2692537