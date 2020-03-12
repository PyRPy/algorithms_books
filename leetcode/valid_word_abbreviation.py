# valid_word_abbreviation.py
class Solution:
    def validWordAbbreviation(self, word, abbr):
        i, j = 0, 0 
        while i < len(abbr):
            if j >= len(word):
                return False 
            if not abbr[i].isdigit():
                if abbr[i] != word[j]:
                    return False 

                i += 1 
                j += 1 
            else:
                if abbr[i] == "0":
                    return False 
                n = ''
                while i < len(abbr) and abbr[i].isdigit():
                    n += abbr[i]
                    i += 1 
                j += int(n)
        return j == len(word)

s = "internationalization"
abbr = "i12iz4n"
sol = Solution()
print(s, " ", abbr)
print(sol.validWordAbbreviation(s, abbr))