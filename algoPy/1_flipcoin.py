# 1_flipcoin.py
import random 

# Simulate a coin flip by writing 'Heads' or 'Tails' to standard
# output.

if random.randrange(0, 2) == 0:
    print('heads')
else:
    print('tails')
# https://introcs.cs.princeton.edu/python/13flow/flip.py.html