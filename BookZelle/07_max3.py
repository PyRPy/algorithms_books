# 07_max3.py
# using decision tree
def main():
    x1, x2, x3 = eval(input("please enter three values: ")) 

    if x1 >= x2:
        if x1 >= x3:
            maxval = x1 
        else: maxval = x3 

    else:
        if x2 >= x3: 
            maxval = x2 
        else:
            maxval = x3 
    
    print("the largest value is", maxval)

main()
