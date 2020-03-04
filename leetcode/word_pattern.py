# word_pattern.py
class Solution:
    def wordPattern(self, pattern, str):
        words = str.split(' ')

        if len(words) != len(pattern):
            return False 
        hashmap = {}
        mapval ={}

        for i in range(len(pattern)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != words[i]:
                    return False 
            else:
                if words[i] in mapval:
                    return False 
                hashmap[pattern[i]] = words[i] 
                mapval[words[i]] = True 
        return True 

pattern = "abba"
str = "dog cat cat dog"

sol = Solution()
print(pattern, " ", str)
print(sol.wordPattern(pattern, str))
