# 11_gpasort.py
# a program to sort student information into GPA order 

from gpa import Student, makeStudent 

def readStudents(filename):
    infile = open(filename, 'r')
    students = [] 
    for line in infile:
        students.append(makeStudent(line)) 
    infile.close() 
    return students 

def writeStudents(students, filename):
    outfile = open(filename, 'w') 
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()), file = outfile)

    outfile.close() 

def main():
    print("this program sorts students grade information by GPA")
    filename = input("enter the name of the data file: ")
    data = readStudents(filename) 
    data.sort(key = Student.gpa) 
    filename = input("enter a name for the output file: ")
    writeStudents(data, filename) 
    print("this data has been written to", filename) 

if __name__ == '__main__':
    main()
