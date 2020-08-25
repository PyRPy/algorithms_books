# 1_selfavoid.py
import sys 
import random 

# Accept integers n and trialCount as command-line arguments. Do
# trialCount random self-avoiding walks in an n-by-n lattice. 
# Write to standard output the percentage of dead ends encountered

n = int(sys.argv[1]) 
trials = int(sys.argv[2]) 
deadEnds = 0 

for t in range(trials):
    a = [[False for x in range(n)] for y in range(n)]
    x = n // 2 
    y = n // 2 
    while x > 0 and x < n-1 and y > 0 and y < n-1:
        a[x][y] = True 
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            deadEnds += 1
            break
        r = random.randrange(1, 5)
        if   (r == 1) and (not a[x+1][y]):
            x += 1
        elif (r == 2) and (not a[x-1][y]):
            x -= 1
        elif (r == 3) and (not a[x][y+1]):
            y += 1
        elif (r == 4) and (not a[x][y-1]):
            y -= 1
print(str(100*deadEnds//trials) + '% dead ends')
# https://introcs.cs.princeton.edu/python/14array/selfavoid.py.html
# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array