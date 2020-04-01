# 05_numbers2text.py
# convert numbers to text !

def main():
    print("convert the numbers to text - Unicode")

    inString = input("pleaes enter the unicode-encoded message: ")

    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)
        message = message + chr(codeNum)

    print("\nThe decoded message is:", message)

main()
