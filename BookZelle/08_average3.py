# 08_average3.py 
# sentinel loops

def main():
    total = 0.0 
    count = 0 
    x = float(input("enter a number (negative to quit) >> ")) 
    while x >= 0: 
        total = total + x 
        count = count + 1 
        x = float(input("enter a number (negative to quit) >> ")) 
        print("\nThe average of the numbers is", total / count) 

main() 
