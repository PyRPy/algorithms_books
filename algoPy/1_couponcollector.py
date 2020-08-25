# 1_couponcollector.py
import sys 
import random 

# Accept integer n as a command-line argument. Write to standard
# output the number of coupons you collect before obtaining one of
# each of n types

n = int(sys.argv[1]) 
count = 0 
collectedCount = 0 
isCollected = n * [False]

while collectedCount < n:
    value = random.randrange(0, n) 
    count += 1 
    if not isCollected[value]:
        collectedCount += 1 
        isCollected[value] = True 
print(count) 
# https://introcs.cs.princeton.edu/python/14array/couponcollector.py.html
