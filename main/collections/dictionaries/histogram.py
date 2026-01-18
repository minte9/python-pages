# -------------------------------
# HISTOGRAM
# -------------------------------
# Problem:
# You have a text input and want to know:
#   - How many times does each character appear?
#
# A histogram counts how many times each item apperas.
# 
# get() avoids errors when the key is missing.

def histogram(text):
    """
    Counts how many times each character appears.
    Returns a dictionary: character -> count
    """
    counts = dict()

    for ch in text:
        if ch not in counts:
            counts[ch] = 1
        else:   
            counts[ch] += 1

    return counts

assert histogram("google") == {'g': 2, 'o': 2, 'l': 1, 'e': 1}


# -------------------------------------
# get(key, default)
# -------------------------------------

h = histogram("yahoo")

assert h.get('o') == 2
assert h.get('x', 0) == 0  # default value if key does not exists


# ---------------------------------------
# PRINTING RESULTS
# ---------------------------------------

h = histogram("google")

for letter in h:  # OR h.keys()
    print(letter + ": " + str(h[letter]))
    # g: 2
    # o: 2
    # l: 1
    # e: 1


# ----------------------------------------
# INVERT HISTOGRAM
# ----------------------------------------
# Turns: letter -> count
# Into: count -> letter

def invert_histogram(d):
    inverted = dict()

    for key in d:
        value = d[key]

        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)

    return inverted

h = invert_histogram(histogram("google"))

for count in h:
    print(count, h[count])
    # 2 ['g', 'o']
    # 1 ['l', 'e']
