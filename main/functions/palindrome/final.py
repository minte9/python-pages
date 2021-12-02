"""Check if string is palindrome
A palindrome is a word that is spelled the same backward and forward.
Example: noon, redivider

Final version: refactoring
"""

def first(word): 
    return word[0]

def last(word): 
    return word[-1]

def middle(word): 
    return word[1:-1]

def is_palindrome(word):
    if (first(word) != last(word)):
        return False
    if (len(word) > 2):   
        return is_palindrome(middle(word))
    return True

assert is_palindrome("noon") == True
assert is_palindrome("redivider") == True
assert is_palindrome("to")  == False
assert is_palindrome("moomm") == False