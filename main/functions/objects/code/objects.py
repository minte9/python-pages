""" In Python, all functions are objects  
    We can easily express constructors difficult to do in other languages
"""

import re

A = [' Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda?', 'south carolina##']


""" Standard approach, applying operations to items
"""

def clear_strings(A):
    result = []
    for v in A:
        v = v.strip()
        v = re.sub('[!#?]', '', v)
        v = v.title()
        result.append(v)
    return result

B = clear_strings(A)
print(B)


""" Using a list of opperations, you can easily modify at a very high level
"""

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

def clear_strings_ops(A, ops):
    result = []
    for v in A:
        for func in ops:
            v = func(v)
        result.append(v)
    return result

B = clear_strings_ops(A, [str.strip, remove_punctuation, str.title])
print(B)


"""
    ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South Carolina']
    ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South Carolina']
"""