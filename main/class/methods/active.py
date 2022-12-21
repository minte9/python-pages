# In functional programming, the function is the active agent:
# Hey print_time! Here's an object to print
#
# In OOP, the objects are the active agents.
# Hey obj start! Please print yourself

class Time:
    
    def set(self, seconds):
        time = Time()
        minutes, time.seconds = divmod(seconds, 60)
        hour, time.minutes = divmod(minutes, 60)
        time.hour = hour
        return time

    def print(self):
        print('%.2d:%.2d:%.2d' % 
            (self.hour, self.minutes, self.seconds)
        )

time = Time()
time.set(160).print() # 00:02:40