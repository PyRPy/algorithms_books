# 05_userfile.py
# creater user names in batch mode
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    """
    this program creates a file of usernames from a file of names
    """

    infileName = askopenfilename()
    outfileName = asksaveasfilename()

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
