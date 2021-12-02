"""Check if string is palindrome
A palindrome is a word that is spelled the same backward and forward.
Example: noon, redivider
We use built-in function len() to check the string length.

Version 2: test first/last
"""

def is_palindrome(word):
    first = word[0]
    last = word[-1]
    if (first != last):
        return False
    return True

assert is_palindrome("abca") == True
assert is_palindrome("abc") == False