# -------------------------------------
# COMPLEX LOOPING
# ------------------------------------- 
# An iterator can be used to implement 
# more complex looping patterns than a for loop.

import json

json_data = """
{
  "name": "John",
  "age": 30,
  "city": "New York",
  "children": [
    {
        "name": "Alice",
        "age": 5
    },
    {
        "name": "Bob",
        "age": 8
    }
  ]
}
"""

def depth_first_traversal(json_obj):
    stack = [json_obj]

    # Loop until there are no iterable elements (such as strings or numbers)
    while stack: 
        
        current = stack.pop()
        yield current

        if isinstance(current, dict):
            stack.extend(current.values())

        elif isinstance(current, list):
            stack.extend(current[::-1]) # new list in reverse order
            
# Parse json
json_obj = json.loads(json_data)

# Display elements
print("Depth-First Traversal:")
for node in depth_first_traversal(json_obj):
    print(node)

"""
Depth-First Traversal:
{'name': 'John', 'age': 30, 'city': 'New York', 'children': [{'name': 'Alice', 'age': 5}, {'name': 'Bob', 'age': 8}]}
[{'name': 'Alice', 'age': 5}, {'name': 'Bob', 'age': 8}]
{'name': 'Alice', 'age': 5}
5
Alice
{'name': 'Bob', 'age': 8}
8
Bob
New York
30
John
"""