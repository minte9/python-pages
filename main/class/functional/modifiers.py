# Modifiers
#
# Functions that modifiy the objects are called modifiers.
#
# Pure functions are faster to develop and less error-prone, but ...
# modifiers are convenient at times and efficient.

class Time: pass

def increment(t, seconds): # modifier
    t.seconds = t.seconds + seconds

def increment_pure(seconds): # pure
    time = Time()
    minutes, time.seconds = divmod(seconds, 60)
    hour, time.minutes = divmod(minutes, 60)
    time.hour = hour
    return time

def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minutes, t.seconds))

t = Time()
t.hour = 9
t.minutes = 45
t.seconds = 0

increment(t, 20)
print_time(t) 
    # 10:45:20

t = increment_pure(160)
print_time(t) 
    # 00:02:40