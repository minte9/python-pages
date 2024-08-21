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

"""
    3 2 1 End
"""