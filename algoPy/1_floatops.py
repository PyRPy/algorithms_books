# https://introcs.cs.princeton.edu/python/12types/floatops.py.html
# here to remove 'stdio.write' is to simplify the code and 
# make it more portable for references

import sys

# Accept two floats a and b as command-line arguments. Use them
# to illustrate float operators. Write the results to standard output.

a = float(sys.argv[1])
b = float(sys.argv[2])

total = a + b
diff  = a - b
prod  = a * b
quot  = a / b
exp   = a ** b

print(str(a) + ' +  ' + str(b) + ' = ' + str(total))
print(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
print(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
print(str(a) + ' /  ' + str(b) + ' = ' + str(quot))
print(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

#-----------------------------------------------------------------------
# python3 floatops.py 123.1 4.55
