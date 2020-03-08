# guess_number.py
class Solution():
    def guessNumber(self, n):
        """
        type n: int 
        rtype: int
        """

        left = 1
        right = n 

        while left <= right:
            mid = (left + right) / 2 
            ret = guess(mid)

            if ret == 0:
                return mid 
            elif ret == -1:
                right = mid - 1
            else:
                left = mid + 1 

n = 10 
sol = Solution()
print(n)
print(sol.guessNumber(n))

# need API to complete programs