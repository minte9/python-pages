# The slice operator [:] works on list
# (same as with strings)
#
# The value -1 refers to the last index in a list

word = "abcde"

assert word[:1] == "a"
assert word[1:] == "bcde"
assert word[1:3] == "bc"    # 3 limit, not included


list = ["a", "b", "c", "d", "e"]

assert list[:1] != "a"
assert list[:1] == ["a"]
assert list[1:] == ["b", "c", "d", "e"]
assert list[1:3] == ["b", "c"]

assert list[-1] == "e"  # last