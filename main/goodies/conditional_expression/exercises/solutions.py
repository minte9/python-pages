""" 1. Use conditional expression to assign a new variable.
       If variable a is greater than 100 assign b to 10, else assign to -1.  
"""

a = 0
b = 100 if a >=0 else -1
print(b) # 100

a = -100
b = 100 if a >=0 else -1
print(b) # -1


""" 2. Define the function to get the factorial of a number.   
       Use conditional expression. 
"""

def factorial(n):
    return 1 if n==0 else factorial(n-1) * n

print("Factorial(0): ", factorial(0))  # 1
print("Factorial(1): ", factorial(1))  # 1
print("Factorial(2): ", factorial(2))  # 2
print("Factorial(2): ", factorial(3))  # 6