def swap_case(s):
    letters = []
    for c in s:
        c = c.capitalize() if c.islower() else c.lower()
        letters.append(c)
    return ''.join(letters)

s = "Hello World!"
print(swap_case(s))  # hELLO wORLD!


# Built-in:
s = "AaZz123!"
print(s.swapcase())  # aAzZ123!