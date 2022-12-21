"""Find text in phone format: 415-555-1234
Not using regex involves a lot of code.
If you want to find a phone within a larger text ...
you would have to add even more code.
"""

def is_phone_number(text):

    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  
    
    if text[7] != '-':
        return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  

    return True

assert is_phone_number('123456789012') == False
assert is_phone_number('123-456-7777') == True
assert is_phone_number('123-4567777') == False

text = """Call me at 123-456-7777 or 415-555-1234, 
but not at 415-5551234."""

for i in range(len(text)):
    chunk = text[i:i+12]
    if is_phone_number(chunk):
        print("Found phone number: " + chunk)
print("Done")

# Found phone number: 123-456-7777
# Found phone number: 415-555-1234
# Done