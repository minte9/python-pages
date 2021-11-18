# You can't use lists with dictionaries
# Insteed, it is common to use tuples

dictonary = {
    ("Johny", "Cash"): 4007344455,
    ("John", "Lennon"): 400768696,
}

for a, b in dictonary:
    print(a, b, dictonary[a, b])
        # Johny Cash 4007344455
        # John Lennon 400768696
