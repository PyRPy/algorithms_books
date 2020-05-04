# 5_convert_integer_string.py
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n] 
    else:
        return toStr(n//base, base) + convertString[n%base] 

print(toStr(1453, 16))

convertString = "0123456789ABCDEF"
print("1453 // 16: ", 1453//16)
print("1453 % 16: ", 1453 % 16)
print(convertString[13])

print("10 to base 2: ", toStr(10, 2))

