""" XSS 
Prevent cross site scriting attacks
The sax library escape should execute faster
"""
from xml.sax.saxutils import escape
from xml.sax.saxutils import quoteattr

a = '< & >'
x = escape(a)

b = "a ' b"
y = quoteattr(b)

assert x == '&lt; &amp; &gt;'
assert y == '"a \' b"'

print('pass')