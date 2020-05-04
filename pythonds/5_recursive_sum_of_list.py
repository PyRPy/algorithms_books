# 5_recursive_sum_of_list.py
# for loop version
def listsum(numList):
    theSum = 0 
    for i in numList:
        theSum = theSum + i 
    return theSum 

print(listsum([1,3,5,7,9]))

def listsumRec(numlist):
    if len(numlist) == 1:
        return numlist[0] 
    else:
        return numlist[0] + listsumRec(numlist[1: ])

print('sum of a list with recursive function: ')
print(listsumRec([1,3,5,7,9]))