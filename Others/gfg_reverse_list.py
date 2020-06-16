# reverse_list.py
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start] 
        start += 1 
        end -= 1 

def reverseList2(A, start, end):
    if start >= end:
        return 
    A[start], A[end] = A[end], A[start] 
    reverseList2(A, start+1, end-1) 

# test 
A = [1, 2, 3, 4, 5, 6] 
print('before reverse: ', A)

reverseList(A, 0, 5) 
print('after reverse: ', A)

reverseList2(A, 0, 5) 
print('after reverse again: ')
print(A)

