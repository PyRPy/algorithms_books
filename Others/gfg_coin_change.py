# gfg_coin_change.py
# recursive method - ask how many ways you can combine coins to get 
# target number 
def count(S, m, n):
    if n == 0:
        return 1 

    if n < 0:
        return 0 

    if m <= 0 and n >= 1:
        return 0 

    return count(S, m-1, n) + count(S, m, n-S[m-1]) 

# test 
arr = [1, 5, 10, 25]
m = len(arr) 
print(count(arr, m, 25))

# https://www.geeksforgeeks.org/coin-change-dp-7/