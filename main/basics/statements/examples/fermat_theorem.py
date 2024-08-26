""" Fermat's Last Theorem (input)

    For any positive integers a, b, c and n > 2
    (a**n + b**n) != c**n
"""

def check_fermat_theorem(a, b, c, n):
    if n <= 2:
        return True

    if ( (a**n + b**n) != c**n):
        return True

    return False

# User input
a, b, c, n = input('Input a b c n:\n').split(' ')
a, b, c, n = int(a), int(b), int(c), int(n)

# Check theorem
if (check_fermat_theorem(a, b, c, n)):
    print('Fermat was right!')
else:
    print('Fermat was wrong')