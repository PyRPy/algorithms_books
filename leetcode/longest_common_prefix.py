class Solution:
	def longestCommonPrefix(self, strs):
		if not strs:
			return ""

		for i in range(len(strs[0])):
			for string in strs[1: ]:
				if i >= len(string) or string[i] != strs[0][i]:
					return strs[0][:i]

		return str[0]

strs = ["flower", "flight", "flow"]
sol = Solution()
print("the string: ", strs)
print("longest common prefix: ", sol.longestCommonPrefix(strs))
