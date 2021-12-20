"""XSS 
Prevent cross site scriting attacks.
Escape xml tags.
"""
from xml.sax.saxutils import escape
from xml.sax.saxutils import quoteattr

s1 = '< & >'
o1 = escape(s1)
print(o1)
    # &lt; &amp; &gt;

s2 = "a ' b"
o2 = quoteattr(s2)
print(o2)
    # "a ' b"


assert o1 == '&lt; &amp; &gt;'
assert o2 == '"a \' b"'

print('pass')