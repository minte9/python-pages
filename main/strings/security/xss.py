"""XSS
Prevent cross site scriting attacks.
Escape html tags with html library.
"""
import html

s1 = """& < " ' >"""
o1 = html.escape(s1)
print(o1)
    # &amp; &lt; &quot; &#x27; &gt;

s2 = "<script>alert('hack');</script>"
o2 = html.escape(s2)
print(o2)
    # &lt;script&gt;alert(&#x27;hack&#x27;);&lt;/script&gt;

assert o1 == '&amp; &lt; &quot; &#x27; &gt;'
assert o2 == '&lt;script&gt;alert(&#x27;hack&#x27;);&lt;/script&gt;'

print("pass")