"""Strong password detection:
At least 8 character long, contains both uppercase and lowercase,
and has at least one digit,
and has at least one non-word character
"""
import re

def password_is_strong(password):
    pattern = r'''(
        (?=.*[a-z]+)    # positive look ahead, at least one lowercase
        (?=.*[A-Z]+)    # positive look ahead, at least one upper case
        (?=.*[\d]+)     # positive look ahead, at least one digit
        (?=.*[\W]+)     # positive look ahead, at least one non-word
        .{8,}           # plus 5 more characters
        )'''
    pattern = re.compile(pattern, re.VERBOSE)
    result = pattern.search(password)
    return result != None

assert password_is_strong("abc") == False
assert password_is_strong("abcdefgh") == False

assert password_is_strong("Abcd2efgh!") == True
assert password_is_strong("aB2&bcde") == True

assert password_is_strong("aBcefg1!") == True
assert password_is_strong("aBcef1!") == False