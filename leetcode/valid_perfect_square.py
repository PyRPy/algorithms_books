# valid_perfect_square.py
class Solution():
    def isPerfectSquare(self, num):
        if num == 1:
            return True 
        left, right = 0, num 
        while left <= right:
            mid = left + (right - left) // 2 
            if mid > num / mid:
                right = mid - 1 
            elif mid == num / mid:
                return True 
            else:
                left = mid - 1 
        return left == num // left and num % left == 0

num = 16 
sol = Solution()
print(num)
print(sol.isPerfectSquare(num))
