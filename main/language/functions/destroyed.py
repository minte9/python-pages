# A function local variable is destroyed ...
# after the function is called

def myfunc(a, b):
    c = a + b
    return c

print(myfunc(3, 4)) # 7

print(c) 
    # NameError: name 'c' is not defined