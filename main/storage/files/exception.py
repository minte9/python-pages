# Exception
# 
# Handling an error with try statement is called ...
# catching an exception.

try:
    fp = open("/var/www/python/") # Error: not a file
except:
    print("Error: not a file")
