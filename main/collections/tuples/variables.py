# Tuple elegant syntax to swap variables
c = 3
d = 4
c, d = d, c
assert (c, d)   == (4, 3)
assert (c)      == 4
assert (c,)     != 4
assert (c, d)   != (3, 4)

# Common method is to use a tmp variable
a = 1
b = 2
tmp = a
a = b
b = tmp
assert (a, b) == (2, 1)

# Example: Split an email address
name, domain = "office@google.com".split('@')
assert (name, domain) == ("office", "google.com")
assert domain == "google.com"