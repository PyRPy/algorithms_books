# reverse integer
class Solution:
    def reverse(self, x):
        num = 0
        a = abs(x)
        while(a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a / 10)

        if x > 0 and num < 2**32 - 1:
            return num
        elif x < 0 and num <= 2**32 - 1:
            return -num
        else:
            return 0
# test
x = 123
sol = Solution()
print('integer :', x, ' reversed: ', sol.reverse(x))
