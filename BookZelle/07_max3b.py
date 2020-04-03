# 07_max3b.py
# sequential processing
def main():
    x1, x2, x3 = eval(input("please enter three values: ")) 

    maxval = x1 
    if x2 > maxval:
        maxval = x2 
    if x3 > maxval:
        maxval = x3
    
    print("the largest value is", maxval)

main()
