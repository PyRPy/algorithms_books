# find_missing_number.py
def getMissingNum(A):
    n = len(A) 
    total = (n + 1) * (n + 2) / 2 
    sumOfA = sum(A) 
    return total - sumOfA  

def getMissingNum2(A):
    i, total = 0, 1 
    for i in range(2, len(A) + 2):
        total += i 
        total -= A[i - 2] 
    return total 

# use XOR
def getMissingNum3(A):
    x1 = A[0] 
    x2 = 1 
    n = len(A)
    for i in range(1, n):
        x1 = x1^A[i] 

    for i in range(2, n +2):
        x2 = x2^i 
    return x1^x2 



# test 
A = [1, 2, 4, 5, 6] 
missingNum = getMissingNum(A) 
print(missingNum) 
print('second method: ')
print(getMissingNum2(A))

print('third method - XOR: ')
print(getMissingNum3(A))

# https://www.geeksforgeeks.org/find-the-missing-number/