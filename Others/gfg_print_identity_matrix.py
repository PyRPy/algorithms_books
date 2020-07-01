# gfg_print_identity_matrix.py  
def Identity(size):
    for row in range(0, size):
        for col in range(0, size):
            if row == col:
                print("1 ", end = " ")
            else: 
                print("0, ", end = " ")
        print() 

# test 
size = 5 
Identity(size)

# https://www.geeksforgeeks.org/program-print-identity-matrix/?ref=rp