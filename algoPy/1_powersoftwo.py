# 1_powersoftwo.py
import sys 

# Accept positive integer n as a command-line argument. Write to
# standard output a table showing the first n powers of two.

n = int(sys.argv[1]) 
power = 1 
i = 0
while i <= n:
    print(str(i) + ' ' + str(power))
    power = 2 * power 
    i = i + 1 

# https://introcs.cs.princeton.edu/python/13flow/powersoftwo.py.html