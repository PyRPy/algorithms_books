# word_search.py
class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):
                    return True 
        return False 

    def helper(self, board, i, j, word, wordIndex):
        if wordIndex == len(word):
            return True 

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[wordIndex] != board[i][j]:
            return False 

        board[i][j] = "#"

        found = self.helper(board, i+1, j, word, wordIndex+1) \
            or self.helper(board, i, j+1, word, wordIndex+1) \
            or self.helper(board, i, j-1, word, wordIndex+1) \
            or self.helper(board, i-1, j, word, wordIndex+1)

        board[i][j] = word[wordIndex]

        return found 

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "SEE"

print(board)
print(word)
sol = Solution()
print(sol.exist(board, word))
