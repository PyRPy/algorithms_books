# code from clrs example code
import os
import re
import math
import time

def binary_search(array, searchingelement):
    last = array.__len__()
    mid = int(last/2)
    min = 0
    for i in range(int(math.log(last)/math.log(2)) + 1):
        if array[mid] == searchingelement:
            return str(mid) + " the index"
        elif array[mid] < searchingelement:
            min = mid
            mid = int((last + mid)/2)
        else:
            last = mid
            mid = int((mid + min)/2)
    return None

if __name__ == '__main__':
    array = []
    for i in range(100000):
        array.append(i)

    t0 = time.perf_counter()
    print(binary_search(array, 345676))
    t1 = time.perf_counter()
    print("binary_search: " + str(t1 - t0))
