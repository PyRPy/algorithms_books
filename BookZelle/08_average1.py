# 08_average1.py
def main():
    n = int(input("how many numbers do you have? "))
    total = 0.0 
    for i in range(n):
        x = float(input("enter a number >> "))
        total = total + x 
    print("\nThe average of the numbers is", total / n) 

main() 