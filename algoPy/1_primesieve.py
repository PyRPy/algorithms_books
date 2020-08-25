# 1_primesieve.py
import sys 

n = int(sys.argv[1]) 

isPrime = (n + 1) * [True]
for i in range(2, n):
    if isPrime[i]:
        for j in range(2, n // i + 1):
            isPrime[i*j] = False 

count = 0 
for i in range(2, n+1):
    if isPrime[i]:
        count += 1 
print('when n <= ' + str(n) + ' there are ' + str(count) + ' prime numbers') 

# https://introcs.cs.princeton.edu/python/14array/primesieve.py.html