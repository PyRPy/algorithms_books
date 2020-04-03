# 07_maxn.py
# find the maximum of a series numbers

def main():
    n = int(input("how many numbers are there? "))

    # set the first number = max 
    maxval = float(input("enter a number >> "))

    # compare the n-1 successive values
    for i in range(n-1):
        x = float(input("enter a number >> ")) 
        if x > maxval:
            maxval = x 

    print("the largest value is", maxval) 

main() 
