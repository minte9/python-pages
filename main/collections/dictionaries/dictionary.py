# ---------------------------------------
# DICTIONARIES
# ---------------------------------------
# A dictionary maps KEYS and VALUES.
# Unlinke lists, keys do NOT have to be integers.
# Keys must be unique and hashable.


# Create an empty dictionary
# --------------------------
prices = dict()

# Add items (product -> price)
prices["apple"] = 0.50
prices["banana"] = 0.30

# Access values using the key
assert prices.get("apple") == 0.50
assert prices.get("orange") == None  # key not found


# Create a dictonary using {}
# ---------------------------
prices = {
    "apple": 0.50,
    "banana": 0.30,
    "orange": 0.80,
}

assert prices["banana"] == 0.30
assert prices["orange"] == 0.80


# ----------------------------------
# CHECKING KEYS
# ----------------------------------

assert "apple" in prices
assert "grape" not in prices


# ----------------------------------
# LOOPING
# ----------------------------------

# Loop througk values
for price in prices.values():
    print(price)
    # 0.5
    # 0.3
    # 0.8

# Loop through keys
for product in prices.keys():
    print(product)
    # apple
    # banana
    # orange

# Loop through keys and values together
for product, price in prices.items():
    print(product, "costs", price)
    # apple costs 0.5
    # banana costs 0.3
    # orange costs 0.8