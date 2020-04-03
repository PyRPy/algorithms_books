# 08_average5.py
# reading numbers from a file 
# end of line - while loop

def main():
    fileName = input("what file are the numbers in? ")
    infile = open(fileName, 'r')
    total = 0.0 
    count = 0 
    line = infile.readline()
    while line != "":
        total = total + float(line) 
        count = count + 1 
        line = infile.readline()  
    print("\nThe average of the numbers is", total / count) 

main() 
