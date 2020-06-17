# gfg_stock_buy_sell.py
def maxProfit(price, start, end):
    if end <= start: 
        return 0 
    profit = 0

    for i in range(start, end, 1):
        for j in range(i+1, end+1):
            if price[j] > price[i]:
                curr_profit = price[j] - price[i] + \
                    maxProfit(price, start, i-1) + \
                    maxProfit(price, j+1, end) 
                profit = max(profit, curr_profit) 
    return profit 

def stockBuySell(price, n):
    if n == 1:
        return 
    i = 0 
    while i < (n -1):
        # find local minima
        while i < n-1 and price[i+1] <= price[i]:
            i += 1 
        if i == n - 1:
            break 

        buy = i # store the index of minima
        i += 1 

        # find local maxima
        while i < n and price[i] >= price[i-1]:
            i += 1 
        sell = i - 1 

        print("buy on day: ", buy, "\t", "sell on day: ", sell) 

# test 
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price) 
print(maxProfit(price, 0, n-1)) 
print('second method: ')
print(stockBuySell(price, n))

# https://www.geeksforgeeks.org/stock-buy-sell/