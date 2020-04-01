# 05_dateconvert.py

# convert "mm/dd/yyy" to "month day, year"

def main():
    dateStr = input("enter a date (mm/dd/yyyy): ")

    # split 
    monthStr, dayStr, yearStr = dateStr.split("/")

    # map str to month name
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    monthStr = months[int(monthStr)-1]
    
    # output in the expected format
    print("the converted date is:", monthStr, dayStr+",", yearStr)

main()
