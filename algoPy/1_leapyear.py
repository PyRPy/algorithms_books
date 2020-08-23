# 1_leapyear.py
import sys 

# Accept an int year as a command-line argument. Write True to
# standard output if year is a leap year.  Otherwise write False.

year = int(sys.argv[1]) 
isLeapYear = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

print('the year {0} is leap year ? {1}'.format(year, isLeapYear))

# python3 1_leapyear.py 2020
# https://introcs.cs.princeton.edu/python/12types/leapyear.py.html