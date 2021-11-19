# Pickle storage:
#
# Databases have a limitation ...
# they works only with strings or bytes.
#
# With pickle module you can convert and store any type.

import os
import dbm
import pickle

DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_DB = DIR + "/db/images_db_pickle"


# Write
# -------------------------------------------
db = dbm.open(IMAGES_DB, 'c')
t = [1, 2, 3]
str = pickle.dumps(t) # b'\x80\x03]q\x00(K\x01K\x02K\x03e.'
db['mylist'] = str
db.close()


# Read
# -------------------------------------------
db = dbm.open(IMAGES_DB, 'r')
b = db['mylist']
str = pickle.loads(b)
assert str == [1, 2, 3]
db.close()


# Object copy
#
# Pickle then revers ....
# has the same effect as copying the object.
#-------------------------------------------
t1 = (1, 2, 3)
str = pickle.dumps(t1)
t2 = pickle.loads(str)

assert t2 == (1, 2, 3)
assert t1 == t2
assert (t1 is t2) == False


# Shelf:
#
# In a 'shelf' db the values can be any objects that pickle can handle.
# --------------------------------------------

import shelve

IMAGES_DB = DIR + "/db/images_db_shelf"

t = (1, 2, 3)
db = shelve.open(IMAGES_DB, 'c')
db['my_tuple'] = t
db.close()

db = shelve.open(IMAGES_DB, 'w')
assert db['my_tuple'] == (1, 2, 3) # pass
db.close()