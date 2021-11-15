# A Caesar cypher is a weak form on encryption:
# It involves "rotating" each letter by a number (shift it through the alphabet)
#
# Example:
# A rotated by 3 is D; Z rotated by 1 is A
# In a SF movie the computer is called HAL, which is IBM rotated by -1
#
# Our function rotate_word() uses:
#   ord (char to code_number)
#   chr (code to char)

def encrypt(word, no):
    rotated = ""
    for i in range(len(word)):
        j = ord(word[i]) + no
        rotated = rotated + chr(j)
    return rotated

def decrypt(word, no):
    return encrypt(word, -no)

assert encrypt("abc", 3) == "def" # pass
assert encrypt("IBM", -1) == "HAL" # pass

assert decrypt("def", 3) == "abc" # pass
assert decrypt("HAL", -1) == "IBM" # pass