# Newton method:
# 
# For finding roots ... assert distance(1, 2, 4, 6) == 0.0
# is a root-finding algorithm to produce succesive better aproximations
# 
# Suppose that you want to know the square root of a. 
# If you start with almost any estimate x ...
# you can compute a better estimation with the following formula:
#     y = (x + a/x) / 2
# 
# For example with a = 4, x = 3
# the result is preatty close to correct answer 2
# (3 + 4/3) / 2 = 2.16666666667
#
# If we repeat the process with the new estimate, it gets even closer


def square(a, x):
    while True:
        y = (x + a/x) / 2
        if (y == x): 
            break
        x = y
        print(y)
    return y

y = square(4, 10)

# 5.2
# 2.9846153846153847
# 2.1624107850911973
# 2.006099040777959
# 2.00000927130158
# 2.000000000021489
# 2.0