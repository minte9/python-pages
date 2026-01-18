# ---------------------------------------
# TUPLES AS DICTIONARY KEYS
# ---------------------------------------
# Tuples are often uses as compound keys.


phonebook = {
    ("Johny", "Cash"): 4007344455,
    ("John", "Lennon"): 400768696,
}

for first, last in phonebook:
    print(first, last, phonebook[first, last])
    # Johny Cash 4007344455
    # John Lennon 400768696
