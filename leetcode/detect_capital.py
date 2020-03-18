# detect_capital.py
class Solution:
    def detectCapitalUse(self, word):
        cap = 0 
        for char in word:
            if char.isupper():
                cap += 1

        if cap == len(word):
            return True 
        elif cap == 0:
            return True 
        elif cap == 1 and word[0].isupper():
            return True 
        else:
            return False 

word = "FlasK"
sol = Solution()
print(word)
print(sol.detectCapitalUse(word))
