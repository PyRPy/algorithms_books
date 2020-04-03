# 08_average2.py
# interactive loops with 'while'
def main():
    total = 0.0 
    count = 0 
    moredata = "yes" 

    while moredata[0] == "y":
        x = float(input("eneter a number >> ")) 
        total = total + x 
        count = count + 1 
        moredata = input("do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", total / count) 

main() 
