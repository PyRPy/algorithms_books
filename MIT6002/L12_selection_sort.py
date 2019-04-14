# selection sort

def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        print('selection sort: ' + str(L))
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
 
testList = [1,3,5,7,2,6,25,18,13]
       
print('')
print(selection_sort(testList))
print(testList)
