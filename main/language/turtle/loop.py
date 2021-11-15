# Square draw - using loop
#
# The syntax of a for statement is similar to a function definition.
# The flow of execution runs through body and then loops back to the top.

import turtle

bob = turtle.Turtle()
print(bob)

def square(bob):
    for i in range(4):
        bob.fd(100) # pixels
        bob.lt(90) # degrees

square(bob)
bob.rt(90)
square(bob)

turtle.mainloop()