# best time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        """
        type prices: list[int]
        rtype: int 
        """
        if len(prices) <= 1:
            return 0
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]

        return total

prices = [10, 21, 23, 28, 10, 15]
sol = Solution()
print(prices)
print(sol.maxProfit(prices)) # maxProfit = 23

