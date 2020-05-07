# 6_selection_sort.py
# make fewer swaps than that in bubble sort

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0 
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionMax]:
                positionOfMax = location 

        temp = alist[fillslot] 
        alist[fillslot] = alist[positionOfMax] 
        alist[positionOfMax] = temp 

alist = [54,26,93,17,77,31,44,55,20]
selectSort(alist) 
print(alist) 
