# Newton method v2
#
# In most programming languages, ...
# it is dangerous to test float equality, ...
# because floating-point values are only approximately right.
#
# It is safer to use the built-in function abs to compute the absolute value,
#
# epsilon: how close is close enought

def square(a, x, epsilon):
    while True:

        y = (x + a/x) / 2
        print(y)
        
        if abs(y - x) < epsilon: 
            break
        x = y

y = square(64, 10, 0.0000001)

# 8.2
# 8.002439024390243
# 8.000000371689179
# 8.000000000000009
# 8.0