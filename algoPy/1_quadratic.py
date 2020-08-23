# 1_quadratic.py
import sys 
import math 

# Accept floats b and c as command-line arguments. Compute the
# the roots of the polynomial x^2 + bx + c using the quadratic
# formula. Write the roots to standard output.

b = float(sys.argv[1])
c = float(sys.argv[2])

discriminant = b * b - 4.0 * c  

if discriminant < 0:
    print('there is no solutions in \'real\' numbers, try again')
else: 
    d = math.sqrt(discriminant)
    print((-b + d) / 2.0)
    print((-b - d) / 2.0)

# https://introcs.cs.princeton.edu/python/12types/quadratic.py.html