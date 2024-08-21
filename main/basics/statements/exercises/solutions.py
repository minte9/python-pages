""" 1. Check if number N against the number 10.
       If N is greater than 10, display a message.
       If N is equal with 10, throw an exception.
       For everything else do nothing.
"""

N = 12
# N = 10
# N = -10

if N > 10:
    print(f"{N} is greater than 10")
elif N == 10:
    raise Exception("N is invalid")
else:  
    pass



""" 2. Write a program that waits for user input.
       The user can type 'quit' for exit the program.
"""

while True:
    user_input = input("> ")
    if user_input == 'quit':
        break
    print(user_input)



""" 3. Use while statement to compute square root of 4.
   The Newthon formula is y = (x + a/x) / 2
   Start from an intial estimation of 3.
"""

def square_root(a, x):
    while True:
        y = (x + a/x) / 2

        if y == x:
            break

        # new estimation
        x = y

        print(y)
    return y
    
y = square_root(4, 3)

import math
assert y == math.sqrt(4)