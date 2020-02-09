# best time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        """
        type prices: list[int]
        rtype: int 
        """
        max_profit, min_price = 0, float("inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

prices = [10, 21, 23, 28, 10, 15]
sol = Solution()
print(prices)
print(sol.maxProfit(prices))

