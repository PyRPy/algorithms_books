# valid anagram
class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        lookup = {}

        for i in s: 
            if i not in lookup:
                lookup[i] = 1 
            else:
                lookup[i] +=1

        for j in t:
            if j not in lookup:
                return False 
            else:
                lookup[j] -= 1

        for k in lookup:
            if lookup[k] != 0:
                return False 

        return True 

s = "rat"
t = "tar"
sol = Solution()
print(s, " ", t)
print(sol.isAnagram(s, t))
