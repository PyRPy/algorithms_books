# threesum.py
# pythonize line #13 #22
# put all the stdlib files in same folder as threesum.py
# 'simple' is king !

import stdio 
import stdarray 
def writeTriples(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] == 0:
                    stdio.writef('%d %d %d \n', a[i], a[j], a[k])

def countTriples(a):
    n = len(a)
    count = 0 
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] + a[k] == 0:
                    count += 1 
    return count 

def main():
    a = stdarray.readInt1D()
    count = countTriples(a)
    stdio.writeln(count)
    if count < 10:
        writeTriples(a) 

if __name__ == '__main__':
    main() 

# https://introcs.cs.princeton.edu/python/41analysis/threesum.py.html
# python threesum.py < 8ints.txt