"""Time delta
Datetime module provides a timedelta data type (duration).
Python knows how many days are in each month, also the leap years.
"""
import datetime, time, sys

"""Future day"""
now = datetime.datetime.now()
future = now + datetime.timedelta(days=1000)
print(now) 
    # 2021-12-09 19:09:26.542590
print(future.year) 
    # 2024

"""You can pause a program until a specific date."""
now = datetime.datetime.now()
tommorrow = now + datetime.timedelta(days=1)
while datetime.datetime.now() < tommorrow:
    try:
        time.sleep(1)
    except KeyboardInterrupt: # Ctrl-C
        sys.exit()