""" XSS
Prevent cross site scriting attacks
Escape html tags with html library
"""
import html

a = """& < " ' >"""
x = html.escape(a)

b = "<script>alert('hack');</script>"
y = html.escape(b)

print(x) # &amp; &lt; &quot; &#x27; &gt;
print(y) # &lt;script&gt;alert(&#x27;hack&#x27;);&lt;/script&gt;