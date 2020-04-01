# 05_change_counter2.py

def main():
    print("change counter\n")
    print("please enter the count of each type.")
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))

    total = quarters * 25 + dimes * 10 + nickles * 5 + pennies 

    print("the total value of your change is ${0}.{1:0>2}".format(total//100, total%100))

main()   
