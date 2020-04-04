# 10_gpa.py
# program to find student with highet GPA 

class Student:
    def __init__(self, name, hours, qpoints): 
        self.name = name 
        self.hours = float(hours) 
        self.qpoints = float(qpoints) 

    def getName(self):
        return self.name 

    def getHours(self): 
        return self.hours 

    def getQPoints(self):
        return self.qpoints 

    def gpa(self):
        return self.qpoints / self.hours 

def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints 
    # return a correponding Student object 
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints) 

def main():
    # open the input file for reading 
    filename = input("enter the name of the grade file: ")
    infile = open(filename, 'r') 

    # set best to be the record for the first student in the infile 
    best = makeStudent(infile.readline())

    # process subsequent lines of the file 
    for line in infile:
        # turn the line into a student record 
        s = makeStudent(line) 
        # if this student is best so far, remember it 
        if s.gpa() > best.gpa():
            best = s 
    
    infile.close() 

    # print information about the best student 
    print("the best student is:", best.getName())
    print("hours:", best.getHours())
    print("GAP:", best.gpa())

if __name__ == '__main__':
    main() 
