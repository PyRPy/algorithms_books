# 05_text2numbes.py
# encode text to numbers 

def main():
    print("this program converts text to numbers !")
    print("of number representing the unicode encoding")

    message = input("please enter the message to encode: ")
    print("\nHere are the unicode codes: ")

    for ch in message:
        print(ord(ch), end = " ")
    
    print()

main()
