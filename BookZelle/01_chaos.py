# chaos.py
# excercise 7
def main():
    """
    a simple program illustrating chaotic behavior
    """

    print("this program illustrates a chaotic function")
    x = eval(input("enter first number between 0 and 1: "))
    y = eval(input("enter second number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x, " ", y)

main()
