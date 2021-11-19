# Method __init__ gets invoked when an object is instantiated
# Method __str__ returns a string representation of an object

class Time:
    def __init__(self, hour=0, min=0, sec=0):
        self.hour = hour
        self.min = min
        self.sec = sec

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.min, self.sec)

time = Time(9, 30)
print(time) # 09:30:00