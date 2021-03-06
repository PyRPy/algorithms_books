# 07_quadratic.py
# find the real roots of a quadratic equation
# the program crashes when it has no solution

import math 

def main():
    print("this program fins the real solutions to a quadratic\n")

    try:
        a = float(input("enter coef a: "))
        b = float(input("enter coef b: "))
        c = float(input("enter coef c: "))

        discrim = b * b - 4 * a * c 

        discRoot = math.sqrt(discrim) 
        root1 = (-b + discRoot) / (2 * a) 
        root2 = (-b - discRoot) / (2 * a) 

        print("\nThe solutions are:", root1, root2)
        
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real roots")
        else:
            print("Invalid coefs given")

    except:
            print("\nSomething went wrong, sorry!")

main()
