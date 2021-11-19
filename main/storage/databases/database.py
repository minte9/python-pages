# Many databases are like dictionaries (map keys to values).
# The biggest difference is that the database is on disk.

import os
import dbm

DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_DB = DIR + "/db/images_db"

db = dbm.open(IMAGES_DB, 'c')
db['myimage.jpg'] = '/images/myimage.jpg'
db['myimage.png'] = '/images/myimage.png'

print(db['myimage.jpg']) 
    # b'/images/myimage.jpg'
    # the result is a bytes object (it begins with b)

db.close()


# You can use dictionaries methods ...
# to loop through items.

db = dbm.open(IMAGES_DB)
for key in db.keys():
    print(key, db[key])
        # b'myimage.png' b'/images/myimage.png'
        # b'myimage.jpg' b'/images/myimage.jpg'

db.close()