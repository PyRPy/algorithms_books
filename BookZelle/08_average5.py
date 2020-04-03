# 08_average5.py
# reading numbers from a file 

def main():
    fileName = input("what file are the numbers in? ")
    infile = open(fileName, 'r')
    total = 0.0 
    count = 0 
    for line in infile:
        # print(line)
        total = total + float(line) 
        count = count + 1 
    print("\nThe average of the numbers is", total / count) 

main() 
