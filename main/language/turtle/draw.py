# Drawing in Python
#
# Create a window with small arrow ...
# that represents the turtle.
#
# To move the turtle forward use fd() method.
# The argument of fd is in pixels, for lt() and rt() in degrees.

import turtle

bob = turtle.Turtle()
print(bob)

bob.fd(100) # pixels
bob.lt(90) # degrees
bob.fd(100)

turtle.mainloop()