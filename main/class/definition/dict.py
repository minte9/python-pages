# Empty class - dict
# An empty class has a dictionary that holds the attributes of the object.

class A(object):
    pass

A = A()
A.__dict__ = {
    'key11': 1,
    'key2': 2,
}

A.__dict__['key2'] = 3
print(A.__dict__['key2']) # 3