# 05_userfile.py
# creater user names in batch mode

def main():
    """
    this program creates a file of usernames from a file of names
    """

    infileName = input("what file are the names in? ")
    outfileName = input("what file should the usernames go in? ")

    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        first, last = line.split()
        uname = (first[0] + last[:7]).lower()
        print(uname, file = outfile)

    infile.close() 
    outfile.close()

main()
