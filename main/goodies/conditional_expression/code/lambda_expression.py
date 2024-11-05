""" Conditional expressions are very useful within lambda expressions
"""

func = lambda x: 'even' if x % 2 == 0 else 'odd'

print( func(2) ) # even
print( func(3) ) # odd