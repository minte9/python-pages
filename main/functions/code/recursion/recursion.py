""" It is legal for a function to call itself 
    It is one of the most magical things a program can do
"""

def countdown(n):
    if n <= 0:
        print ("End")
    else:
        print(n, end=" ")
        countdown(n-1)

countdown(3)


""" It is easier to write a for loop, but there are times when we need recursion
"""

def repeat(s, n):
    if n <=0 :
        return
    print(s, end=" ")
    repeat(s, n-1)

repeat('abc', 3)


"""
    3 2 1 End
    abc abc abc
"""