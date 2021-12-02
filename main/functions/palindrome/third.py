"""Use incremental development to check if string is palindrome
A palindrome is a word that is spelled the same backward and forward.
Example: noon, redivider

Version 3: test middle
"""

def is_palindrome(word):
    if (word[0] != word[-1]):
        return False
    if (len(word) > 2):
        middle = word[1:-1]
        return is_palindrome(middle)
    return True

assert is_palindrome("abcba") == True
assert is_palindrome("abca") == False