# 05_numbers2text2.py
# use a list accumulator - more efficient 

def main():
    inString = input("please enter the unicode-message: ")
    chars = []
    for numStr in inString.split():
        codeNum = int(numStr)
        chars.append(chr(codeNum))

    message = "".join(chars)
    print("\nThe decoded message is:", message)

main()
