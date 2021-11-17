# Incremental development - check if string is palindrome
#
# A palindrome is a word that is spelled the same backward and forward
# Example: noon, redivider
#
# We use built-in function len() to check the string length


# FIRST implementation:
# -------------------------------------
#   - define function

def is_palindrome(word):
    return True

assert is_palindrome("abc") == True


# SECOND:
# -------------------------------------
#   - test first/last

def is_palindrome(word):
    first = word[0]
    last = word[-1]
    if (first != last):
        return False
    return True

assert is_palindrome("abca") == True
assert is_palindrome("abc") == False


# THIRD:
# -------------------------------------
#   - test middle

def is_palindrome(word):
    if (word[0] != word[-1]):
        return False
    if (len(word) > 2):
        middle = word[1:-1]
        return is_palindrome(middle)
    return True

assert is_palindrome("abcba") == True
assert is_palindrome("abca") == False


# FINAL:
# -------------------------------------
#   - refactoring


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