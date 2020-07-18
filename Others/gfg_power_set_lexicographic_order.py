# gfg_power_set_lexicographic_order.py
def permuteRec(string, n, index = -1, curr = ""):
    # base case 
    if index == n:
        return 
    if len(curr) > 0:
        print(curr) 

    for i in range(index + 1, n):
        curr += string[i] 
        permuteRec(string, n, i, curr) 

        # backtracking 
        curr = curr[:len(curr) - 1] 
        print('backtracking step: ', curr)

def powerSet(string):
    string = ''.join(sorted(string)) 
    print('print first :', string) 
    permuteRec(string, len(string)) 

# test 
string = 'cab' 
powerSet(string) 
