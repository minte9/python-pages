# A dictonary represents a mapping ...
# from keys to valuess
# 
# In a list, the index have to be integer ...
# in a dictionary it can be any type.


# Create a dictionary using dict()

D = dict()
D["one"] = "uno"

assert D.get("one") == "uno"
assert D.get("one") != None
assert D.get("one") != "one"


# Creates a dictionary using {}

D = {
    "one": "uno",
    "two": "dos",
    "three": "tres",
}

assert D.get("two") == "dos"
assert D["two"] == "dos"


# in operator

assert "one" in D
assert ("dos" in D) == False
assert ("two" in D) == True


# Loop

for v in D.values():
    print(v)
        # uno
        # dos
        # tres

for k in D.keys():
    print(k)
        # one
        # two
        # three