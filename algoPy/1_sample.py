# 1_sample.py
import sys 
import random 

# Accept integers m and n as command-line arguments. Write to standard
# output a random sample of m integers in the range 0...n-1 (no
# duplicates)

m = int(sys.argv[1]) 
n = int(sys.argv[2]) 

perm = n * [0]
print(perm)
for i in range(n):
    perm[i] = i 

for i in range(m):
    r = random.randrange(i, n)
    perm[i], perm[r] =  perm[r], perm[i] # randomly swap two numbers...

for i in range(m):
    print(str(perm[i]) + ' ')
    # print() 
