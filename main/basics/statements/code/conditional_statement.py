""" Conditional statement
    We can check condtions and change the behavior
"""

n = 20

if n % 10 == 0:
    print("n is divisible by 10")
elif n % 10 > 0:
    print("n is not divisible by 10") 
else:
    pass


# Conditional expression (more concisely)
a = 0
msg = "positive" if a >= 0 else "negative"
print("a is", msg)


# Conditional expressions are very useful within lambda expressions
func = lambda x: 'even' if x % 2 == 0 else 'odd'
print(func(2))
print(func(3))