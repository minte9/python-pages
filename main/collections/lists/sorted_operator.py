""" LISTS - SORTED operator
---------------------------
Return a sorted list of the specified iterable object.
Example:
 - Find the students having the second lowest grade.
"""

records = [["John", 20.0], ["Ana", 50.0], ["Marry", 50.2], ["Bob", 50.2]]

scores = [s for n,s in records]  # List comprehension
scores = set(scores)  # Sets automatically remove duplicates

second_minim = sorted(scores)[1]
print(second_minim)  # 50
