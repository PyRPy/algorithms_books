# gfg_is_markov_matrix.py
def checkMarkov(m):
    for i in range(0, len(m)):
        # find the row sum 
        sm = 0 
        for j in range(0, len(m[i])):
            sm = sm + m[i][j] 

        if sm != 1 :
            return False 
    return True 

# test 
m = [ [ 0, 0, 1 ], 
      [ 0.5, 0, 0.5 ], 
      [ 1, 0, 0 ] ] 

if checkMarkov(m):
    print('it is a markov matrix')
else:
    print('it is not a marlov matrix')

# https://www.geeksforgeeks.org/markov-matrix/