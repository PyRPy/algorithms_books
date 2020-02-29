# add_digits.py
class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 0:
            return 0

        else:
            result = (num - 1) % 9 + 1 
        
        return result 

num = 383 
sol = Solution()
print(num)
print(sol.addDigits(num))
# think about it again !