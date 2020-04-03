# 08_average3.py 
# sentinel loops / empty string

def main():
    total = 0.0 
    count = 0 
    xStr = input("enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        total = total + x 
        count = count + 1 
        xStr = input("enter a number (<Enter> to quit) >> ") 
        print("\nThe average of the numbers is", total / count) 

main() 
