""" LISTS - SORTED operator
---------------------------
Return a sorted list of the specified iterable object.
Example: 
- Find the students having the second lowest grade.
----------------------------------------------------
"""

records = [["John", 20.0], ["Ana", 50.0], ["Marry", 50.0], ["Bob", 50.2]]

scores = [s for n,s in records]  # List comprehension
scores = set(scores)             # Sets automatically remove duplicates

second_minim = sorted(scores)[1] # sorted, second

result = [
    name 
    for name, score in records 
    if score == second_minim
]

print(second_minim)  # 50
print(result)        # [Ana, Marry]