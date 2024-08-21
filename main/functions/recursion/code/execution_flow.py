""" Recursion / Execution Flow
"""

def countdown(n):
    if n <= 0:
        print ("End")
    else:
        print(n, end=" ")
        countdown(n-1)

countdown(3)   # 3 2 1 End

"""
    countdown executions begins with n=3 ...
    since n is greater than 0 it outputs 3 ..
    then it calls itself ...

        countdown executions begins with n=2 ...
        since n is greater than 0 it outputs 2 ..
        then it calls itself ...

            countdown executions begins with n=1 ...
            since n is greater than 0 it outputs 1 ..
            then it calls itself ...

                countdown executions begins with n=0 ...
                since n is not greater than 0 it outputs Time! ..
                then returns ...

            the countdown that got n=1 returns

        the countdown that got n=2 returns

    the countdown that got n=3 returns

    After that we are back in the __main__
"""