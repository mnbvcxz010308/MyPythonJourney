#!/usr/bin/python3.5

# read the lines from the file
a = 23 
b = 17 
quot = a//b 
remain = a - (int(quot) * b) 
quotrem = (quot, remain) 
del a,b,quot,remain
print(quotrem)
quotrem = divmod(23,17)
print(quotrem)