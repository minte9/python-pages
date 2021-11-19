# Normal use of a for loop ...
#
# without list comprehension

str = "abc"
res = []

for s in str:
    res.append(s.capitalize())

assert res == ['A', 'B', 'C']