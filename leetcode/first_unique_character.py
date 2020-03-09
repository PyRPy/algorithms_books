# first_unique_character.py
class Solution:
    def firstUniqChar(self, s):
        from collections import Counter
        lookup = Counter(s)

        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i 

        return -1 

    def firstUniqChar2(self, s):
        lookup = dict()
        for i in s:
            if i in lookup:
                lookup[i] += 1 
            else:
                lookup[i] = 1

        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i 
        return -1 



s = "leetcode"
sol = Solution()
print(s)
print("solution 1: ", sol.firstUniqChar(s))
print("solution 2: ", sol.firstUniqChar2(s))
