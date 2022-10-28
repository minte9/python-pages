"""Find text in phone format: 415-555-1234
Use regular expression patterns.
The group() method returns the match.
The findAll() method returns a list of strings.
"""
from nis import match
import re


# Check if string is phone number

def is_phone_number(text):
    pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    result = pattern.search(text)
    if result == None:
        return False
    return True

assert is_phone_number('123456789012') == False
assert is_phone_number('123-456-7777') == True
assert is_phone_number('123-4567777') == False


# Search phone numbers in a text

text = 'Call me at 123-456-7777 or 415-555-1234, but not at 415-5551234.'

def search_first_number(text):
    pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    result = pattern.search(text)
    return result.group()

def search_all_numbers(text):
    pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    result = pattern.findall(text)
    return result

print("First number: " + search_first_number(text))
    # First number: 123-456-7777

numbers = search_all_numbers(text) # list of strings
print("Numbers: \n" + '\n'.join(numbers))
    # Numbers: 
    # 123-456-7777
    # 415-555-1234

pattern = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = pattern.search('111-222-4444')
print(result.group())
    # 111-222-4444