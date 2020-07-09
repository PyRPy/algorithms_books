# gfg_search_word_2D_grid.py 
class Word:
    def __init__(self):
        self.R = None 
        self.C = None 
        self.dir = [[-1, 0], [1, 0], [1, 1], [1, -1],
                    [-1,-1], [-1, 1], [0, 1], [0, -1]]

    # search in 8 directions 
    def search2D(self, grid, row, col, word):
        if grid[row][col] != word[0]:
            return False 

        for x, y in self.dir:
            rd, cd = row + x, col + y 
            flag = True 

        for k in range(1, len(word)):
            if 0 <= rd < self.R and 0 <= cd < self.C and word[k] == grid[rd][cd]:
                rd += x 
                cd += y 
            else: 
                flag = False 
                break 
        if flag:
            return True 
        return False 
        
    def patternSearch(self, grid, word):
        self.R = len(grid) 
        self.C = len(grid[0]) 

        for row in range(self.R):
            for col in range(self.C):
                if self.search2D(grid, row, col, word):
                    print('pattern found at ' + str(row) + ', ', str(col))

# test 
if __name__ == '__main__':
    grid = ["GEEKSFORGEEKS", 
			"GEEKSQUIZGEEK", 
			"IDEQAPRACTICE"] 
    word = Word() 
    word.patternSearch(grid, 'GEEKS')
    print('')
    word.patternSearch(grid, 'EE')

            