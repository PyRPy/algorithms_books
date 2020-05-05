# 6_sequential_search.py
def sequentialSearch(alist, item):
    pos = 0 
    print("start position at: ", pos)
    found = False 

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True 
        else: 
            pos = pos + 1 
        print("search next position at: ", pos)
    return found 

testlist = [1,2,32,8,17,19,42,13,0]
print(sequentialSearch(testlist, 19))
        