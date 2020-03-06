# reverse_vowels_string.py
class Solution:
    def reverseVowels(self, s):
        vowels = "aeiou"
        string = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if string[i].lower() not in vowels:
                i += 1 
            elif string[j].lower() not in vowels:
                j -= 1 
            else: 
                string[i], string[j] = string[j], string[i] 
                i += 1 
                j -= 1 
        return "".join(string)

s = "hello"
sol = Solution()
print(s)
print(sol.reverseVowels(s))
