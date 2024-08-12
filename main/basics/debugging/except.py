# Errors can be handled with ...
# try and except statements.

def calc(number, divider):
    try:
        return number/divider
    except ZeroDivisionError:
        print('Error: Division by zero')
    except:
        print('Error: Invalid argument')

assert calc(10, 2) == 5
assert calc(10, 0) == None  # pass
    # Error: Division by zero