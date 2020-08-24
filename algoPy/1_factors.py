# 1_factors.py
import sys 

# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.

n = int(sys.argv[1]) 
factor = 2 
while factor * factor <= n:
    while n % factor == 0:
        n //= factor 
        print(str(factor) + ' ')
    factor += 1 

if n > 1:
    print(n) 
print()
# https://introcs.cs.princeton.edu/python/13flow/factors.py.html