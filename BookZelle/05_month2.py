# 05_month2.py
# using list of strings to map the input number

def main():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("enter a month number (1-12): "))
    print("the month abbreviation is", months[n-1] + ".")

main()
