"""Datetime
Display today date (year, month, day, etc)
The datetime has its own datatime data type.
"""
import datetime

# now
now = datetime.datetime.now()
print(now) 
    # 2021-12-09 18:56:45.224853

# date
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
assert dt.month == 10
assert dt.day == 21
assert dt.second == 0