""" Recursion / Execution Flow
"""

def countdown(n):
    if n <= 0:
        print ("End")
    
    print(n, end=" ")
    countdown(n-1)

countdown(3)   # 3 2 1 End

"""
    countdown executions begins with n=3 ...
    since n is greater than 0 it outputs n (3) ..
    then it calls itself ...

        begins with n=2 ...
        since n > 0 it outputs n (2) ..
        then it calls itself ...

            begins with n=1 ...
            since n > 0 it outputs n (1) ..
            then it calls itself ...

                begins with n=0 ...
                since n <= 0 it outputs End ..
                then returns None

            the countdown that got n=1 returns

        the countdown that got n=2 returns

    the countdown that got n=3 returns

    After that we are back in the __main__
"""