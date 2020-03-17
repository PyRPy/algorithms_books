# keyboard_row.py
class Solution:
    def findWords(self, words):
        top = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        middle = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        bottom = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        rows = [top, middle, bottom]

        output = []

        for word in words:
            for row in rows:
                if word[0].lower() in row:
                    result_row = row 
                    break 
            for char in word:
                j = 0 
                if char.lower() not in result_row:
                    j = -1
                    break 
            if j != -1:
                output.append(word)

        return output 

words = ["Hello", "Alaska", "Dad", "Peace"]
sol = Solution()
print(words)
print(sol.findWords(words))
