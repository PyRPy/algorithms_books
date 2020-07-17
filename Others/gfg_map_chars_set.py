# gfg_map_chars_set.py
def newString(charSet, input):
    origCharset = 'abcdefghijklmnopqrstuvwxyz'
    mapChars = dict(zip(charSet, origCharset)) 

    changeChars = [mapChars[chr] for chr in input] 
    print(''.join(changeChars)) 

# test 
charSet = 'qwertyuiopasdfghjklzxcvbnm'
input = 'utta' 
newString(charSet, input) 
# https://www.geeksforgeeks.org/zip-function-python-change-new-character-set/
