""" 1. Check if number N against the number 10.
       If N is greater than 10, display a message.
       If N is equal with 10, throw an exception.
       For everything else do nothing.
"""

N = 12
# N = 10
# N = -10

if N > 10:
    print("N is greater than 10")
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