""" While statement
    The syntax is similar to a function definition.

    You can almost read while statement as if it were English:
        - while n is greater than 0
        - display n
        - then decrement it
"""

def countdown(n):
    while(n > 0):
        print(n)
        n = n -1

countdown(5)