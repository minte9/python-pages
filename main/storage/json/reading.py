"""Json read:
Json string always uses double quotes.
The loads() methods return json as a Python dictionary.
The loads() method means 'load string' not 'loads'
"""
import json

str = '{"name":"John", "age":40, "job":null}'
dict = json.loads(str)

assert dict.get('name') == 'John'
assert dict.get('age') == 40
assert dict.get('job') == None