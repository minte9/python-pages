# Methods are functions defined inside a class

class Time: 
    def print(self):
        print('%.2d:%.2d:%.2d' % 
            (self.hour, self.minute, self.second)
        )

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

# Invoking a method is different from calling a function

Time.print(start) # 09:45:00