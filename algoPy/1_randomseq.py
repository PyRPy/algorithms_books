# 1_randomseq.py
import sys 
import random 

# Accept integer command-line argument n. Write to standard output
# a random sequence of n floats in the range [0, 1).

n = int(sys.argv[1]) 
for i in range(n):
    print(random.random()) 
    