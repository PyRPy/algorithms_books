# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:57:32 2019

chapter 4 quick sort
"""

def quicksort(array) :
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1: ] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 5, 2, 100, 3]))


#P4.1
def listsum (mylist):   
        if mylist == [] :
            return 0
        else :
             lsum = mylist[0] + listsum(mylist[1:])
        return lsum 

  
                   
# test for loop
mylist=[1, 2, 3]
listsum(mylist) 

for i in mylist :
    print (i)

# answer from book for 4.1
def sumlist(list):
    if list==[]:
        return 0
    return list[0] + sumlist(list[1:])


sumlist(mylist)