# plus one - digits

class Solution:
    def plusOne(self, digits):
        """
        :type digits: list[int]
        :rtype : list[int]
        """

        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits 
        digits[0] = 1
        digits.append(0)
sol = Solution()
digits = [1,9,9,9]
print(digits)
print(sol.plusOne(digits))
