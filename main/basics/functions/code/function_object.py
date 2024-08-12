""" In Python, functions are objects.
    We can easily express constructors difficult to do in other languages.
"""

import re

states = [' Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda?', 'south carolina##']

# A. Standard approach, applying operations to items
def clear_strings(A):
    result = []
    for v in A:
        v = v.strip()
        v = re.sub('[!#?]', '', v)
        v = v.title()
        result.append(v)
    return result

B = clear_strings(states)
print(B)


# B. Using a list of opperations, you can easily modify at a very high level
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

def clear_strings_ops(A, ops):
    result = []
    for v in A:
        for func in ops:
            v = func(v)
        result.append(v)
    return result

B = clear_strings_ops(states, [str.strip, remove_punctuation, str.title])
print(B)

"""
    ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South Carolina']
    ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South Carolina']
"""