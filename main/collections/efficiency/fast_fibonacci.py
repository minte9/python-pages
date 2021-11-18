# Fast (recursion & dictionary)
#
#    fb(0) = 0
#    fb(1) = 1
#    fb(n) = fb(n-1) + fb(n-2)
#
# To make the algorith run faster ...
# one solution is to keep track of values and store them in a dictionary.

loops = 0
known = {0:0, 1:1}

def reset():
    loops = 0
    known = {0:0, 1:1}

def fibonacci(n):

    global loops; 
    loops = loops + 1
    
    if n in known: 
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

reset(); assert fibonacci(4) == 3;           print (loops) # 7
reset(); assert fibonacci(5) == 5;           print (loops) # 10
reset(); assert fibonacci(6) == 8;           print (loops) # 13

fibonacci(1000)
print (loops) # 2002 - Look Here