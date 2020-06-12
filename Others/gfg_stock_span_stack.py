# gfg_stock_span_stack.py
# stack based method 
def calculateSpan(price, S):
    n = len(price) 
    st = [] 
    st.append(0) 
    S[0] = 1 # first element == 1 
    
    for i in range(1, n):
        while len(st) > 0 and price[st[-1]] <= price[i]:
            st.pop() 
        S[i] = i + 1 if len(st) <=0 else i - st[-1] 
        st.append(i) 

def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end = " ")

# test 
price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price))] # why len(price) + 1 , '+1' removed
print(S)
calculateSpan(price, S) 
print(S)
# https://www.geeksforgeeks.org/the-stock-span-problem/