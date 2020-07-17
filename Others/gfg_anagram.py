# gfg_anagram.py
def isAnagram(str1, str2):
    n1 = len(str1) 
    n2 = len(str2) 

    if n1 != n2:
        return False 

    str1 = sorted(str1) 
    str2 = sorted(str2) 

    for i in range(0, n1):
        if str1[i] != str2[i]:
            return False 

    return True 

# method 2
NO_OF_CHARS = 256
def isAnagram2(str1, str2):
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    for i in str1:
        count1[ord(i)] += 1 
    for i in str2:
        count2[ord(i)] += 1 

    if len(str1) != len(str1):
        return False 

    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False 

    return True 

# test 
str1 = "listen"
str2 = "silent"

if isAnagram(str1, str2):
    print('the two strings are anagram')
else:
    print('the two strings are not anagram')

print('this is method 2: ')
if isAnagram2(str1, str2):
    print('the two strings are anagram')
else:
    print('the two strings are not anagram')
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
# maybe translated from other major languages, not written in python from beginning



