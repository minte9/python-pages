# Recursion:
#
# A function can call himself

def countdown(n):
    if n <= 0:
        print ("Time!")
    else:
        print(n)
        countdown(n-1)

countdown(3)

# 3
# 2
# 1
# Time!