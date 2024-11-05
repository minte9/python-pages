""" 1. Catch a division by zero error
"""

try:
    a = 1/0
except ZeroDivisionError:
    print("Division by zero error")
except:
    print("Error")

"""
    Division by zero error
"""