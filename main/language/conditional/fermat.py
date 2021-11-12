# For any number > 2 there are no positive integers a, b, c so that ...
# a**n + b**n = c**n

def fermat_was_right(a, b, c, n):
    if n <= 2:
        return True
    else:
        if (a**n + b**n == c**n):
            return False
    return True

def prompt():
    a = int(input('Input a? '))
    b = int(input('Input b? '))
    c = int(input('Input c? '))
    n = int(input('Input n? '))

    if (fermat_was_right(a, b, c, n)):
        print('Fermat was right!')
    else:
        print('Fermat was wrong')

prompt()