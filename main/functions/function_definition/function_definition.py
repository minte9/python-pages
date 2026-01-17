""" FUNCTION DEFINITION - Leap year example
-------------------------------------------
"""

def is_leap(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    
    return False

assert is_leap(2000) == True
assert is_leap(2400) == True

assert is_leap(1800) == False
assert is_leap(1900) == False
assert is_leap(2100) == False
assert is_leap(2200) == False
assert is_leap(2300) == False
assert is_leap(2500) == False

print("Tests passed")