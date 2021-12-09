"""Json write:
The method dumps() mean 'dump string' not 'dumps'
"""
import json

dict = {"name":"John", "age":40, "job":None}
json = json.dumps(dict)

assert json == '{"name": "John", "age": 40, "job": null}'
assert json != {"name": "John", "age": 40, "job": None}
assert json != '{"name": "John", "age": 40, "job": None}'