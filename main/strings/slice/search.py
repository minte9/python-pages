# Find key in a string

def find_key(str, ch):
    i = 0
    while i < len(str):
        if str[i] == ch:
            return i
        i = i + 1
    return -1

print(find_key("Hello World", "o"))  # 4