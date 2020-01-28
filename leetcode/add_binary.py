# add binary
class Solution:
    def addBinary(self, a, b):
        """
        type a: str
        type b: str
        rtype: str
        """

        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry 
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry, val = val//2, val%2
            result += str(val)
        if carry:
            result += str(1)
        return result[::-1]

a = "1010"
b = "1011"

sol = Solution()
print(a, b)
print('a + b: ', sol.addBinary(a, b))
