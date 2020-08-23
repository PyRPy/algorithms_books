import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

total = a +  b
diff  = a -  b
prod  = a *  b

quot  = a // b
# In Python 2.x, / does classic division and // does floor division
# In Python 3.x, / does true division and // does floor division
# It's wise to use // to divide integers, and / to divide floats.

rem   = a %  b
exp   = a ** b

print(str(a) + ' +  ' + str(b) + ' = ' + str(total))
print(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
print(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
print(str(a) + ' // ' + str(b) + ' = ' + str(quot))
print(str(a) + ' %  ' + str(b) + ' = ' + str(rem))
print(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

# python3 intops.py 1234 5