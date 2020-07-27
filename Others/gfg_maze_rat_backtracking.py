# gfg_maze_rat_backtracking 

N = 4 

# print matrix 
def printSol(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end = "")
        print("")

# valid matrix or not 
def isSafe(maze, x, y):
    if x >= 0 and x < N and y >=0 and y < N and maze[x][y] == 1:
        return True 
    return False 

def solveMaze(maze):
    sol = [[0 for j in range(N)] for i in range(N)] 
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Solution does't exist")
        return False 

    printSol(sol) 
    return True 

# recursive helper function 
def solveMazeUtil(maze, x, y, sol):
    if x == N -1 and y == N - 1 and maze[x][y] == 1:
        sol[x][y] = 1 
        return True 

    if isSafe(maze, x, y) == True:
        sol[x][y] = 1 
        if solveMazeUtil(maze, x+1, y, sol) == True:
            return True 
        if solveMazeUtil(maze, x, y + 1, sol) == True:
            return True 
        
        # backtracking step 
        sol[x][y] = 0 
        return False 

# test 
if __name__ == "__main__":
    maze = [ [1, 0, 0, 0], 
			[1, 1, 0, 1], 
			[0, 1, 0, 0], 
			[1, 1, 1, 1] ] 
    solveMaze(maze) 

# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/