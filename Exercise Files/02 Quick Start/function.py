#!/usr/bin/python3
"""
def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False
    else:
        print(n, "is a prime number")
        return True

for n in range(1,10):
    isprime(n)

"""
import sys
from operator import itemgetter
n,m = map(int, sys.stdin.readline().strip().split())
friends = map(int, sys.stdin.readline().strip().split())
f=[]
for i in range(m):
    f.append(sys.stdin.readline().strip().split())
for i in range(len(f)):
    f[i][0]=int(f[i][0])
    f[i][1]=int(f[i][1])
highest = []
normal=[]
for i in f:
    if i[0] in friends:
        highest.append(i)
    else:
        normal.append(i)
highest = sorted(highest, key=itemgetter(1), reverse=True)
normal = sorted(normal, key=itemgetter(1), reverse=True)
for i in highest:
    sys.stdout.write(i[2]+'\n')
for i in normal:
    sys.stdout.write(i[2]+'\n')
     