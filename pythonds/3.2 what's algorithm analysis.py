# 3.2 what's algorithm analysis
def sumOfN(n):
    theSum = 0 
    for i in range(1, n+1):
        theSum = theSum + i 
    return theSum 

print(sumOfN(10))

import time 

def sumOfN2(n):
    start = time.time() 

    theSum = 0 
    for i in range(1, n+1):
        theSum = theSum + i 
    end = time.time() 
    return theSum, end-start 

print(sumOfN2(10))

for i in range(5):
    print("sum is %d required %10.7f seconds"%sumOfN2(100000))

def sumOfN3(n):
    start = time.time()
    theSum = n * (n + 1)/ 2
    end = time.time()
    return theSum, end - start 
  
print()

for i in range(5):
    print("sum is %d required %10.7f seconds"%sumOfN3(100000))