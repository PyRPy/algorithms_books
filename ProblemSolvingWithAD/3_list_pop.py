# 3_list_bigO.py

# to show the speed when pop(0) or pop() 
# has memory error during the run !

from timeit import *

popzero = Timer("x.pop(0)", "from __main__ import x")

popend = Timer("x.pop()", "from __main__ import x") 

print("pop(0)  pop()")

for i in range(10000, 1000001, 10000):
    x = list(range(i)) 
    pt = popend.timeit(number = 1000) 

    x = list(range(i)) 
    pz = popzero.timeit(number = 1000) 
    print("%15.5f, %15.5f" %(pz, pt))



