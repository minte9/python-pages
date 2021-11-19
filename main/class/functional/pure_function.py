# A pure function ...
# 
# does not modify any of the objects passed and ...
# has no side effects, like displaying a value or getting an input


class Hour:
    """Represents the day time
    attributes: hour
    """

def increment_pure(t, d):
    sum = Hour()
    sum.hour = t.hour + d.hour    
    return sum

def increment_impure(t, d):
    sum = Hour()
    sum.hour = t.hour + int(d.hour) # Look Here    
    return sum

start = Hour()
start.hour = 9.0
duration = Hour()
duration.hour = 1.5

end = increment_pure(start, duration) # Correct
assert end.hour == 10.5
assert end.hour != 10

end = increment_impure(start, duration) # Wrong
assert end.hour != 10.5
assert end.hour == 10


# Side efects

end = increment_pure(start, duration) # Correct

def print_time(obj): # impure - side efects
    print('%.2d' % obj.hour) # 2 digits
    
print_time(end) # 10