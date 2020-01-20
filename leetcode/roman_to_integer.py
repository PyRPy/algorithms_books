# roman to integer
class Solution:
	def romanToInt(self, s):

		numerical_map = {"I": 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100,  "D" : 500, "M" : 1000}
		result = 0

		for i in range(len(s)):
			if i > 0 and numerical_map[s[i]] > numerical_map[s[i - 1]]:
				result = numerical_map[s[i]] - 2 * numerical_map[s[i-1]]
			else:
				result += numerical_map[s[i]]

		return result

s = "XXVII"
sol = Solution()
print("s :", s, "as integer is: ", sol.romanToInt(s))
