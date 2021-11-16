# It is easier to write a for loop ...
# but there are times when we need recursion.

def repeat(s, n):
    if n <=0 :
        return
    print(s)
    repeat(s, n-1)

repeat('abc', 3)
    # abc
    # abc
    # abc