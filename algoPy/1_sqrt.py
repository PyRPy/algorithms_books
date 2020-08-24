# 1_sqrt.py
import sys 

# Accept float c as a command-line argument. Write to standard
# output the square root of c to 15 decimal places of accuracy.
# Use Newton's method.

EPSILON = 1e-15 

c = float(sys.argv[1]) 
if c > 0: 
    t = c  
    while abs(t - c/t) > EPSILON * t:
        t = (c/t + t) / 2.0 
    print(t) 
elif c == 0:
    print(0) 
else:
    print('negative number: no root !')

# https://introcs.cs.princeton.edu/python/13flow/sqrt.py.html