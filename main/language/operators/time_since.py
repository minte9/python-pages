# The time module provides a function ...
# that returns the current GMT in “the epoch”
#
# Let's write a function that returns ...
# days, hours, minutes, seconds since Unix birthday 01.01.1970

import time

today = time.time()
print(today)
    # 1636720824.934335

def convert_GMT(t):

    days = int(t) // (3600 * 4)
    remainder = int(t) % (3600 * 4)

    hours = remainder // 3600
    remainder = remainder % 3600

    minutes = remainder // 60
    remainder = remainder % 60

    seconds = remainder

    return (
        str(days) + " days " + \
        str(hours) + " hours " + \
        str(minutes) + " minutes " + \
        str(seconds) + " seconds"
    )

print(convert_GMT(today))
    # 113661 days 0 hours 50 minutes 32 seconds