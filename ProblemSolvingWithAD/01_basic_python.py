# 01_basic_python.py 

# 1.7. Review of Basic Python
print('Algo and Data Structure')

# atomic data types
print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)

True
False

False or True 
True and True

print(5==10)
print(10>5)
print((5>=1) and (5 <= 10))

theSum = 0 
theSum

# build-in collection data type
[1,3,True,6,5]

myList = [1,3,True,6,5]
myList

myList = [0] * 6 
myList

myList = [1,2,3,4]
A = [myList] * 3 
print(A)

myList[2] = 45
print(A) # interesting 

# list methods
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)

myList.insert(2,4.5)
print(myList)

print(myList.pop(1))
print(myList.pop(0))

myList.sort()
print(myList)

myList.reverse()
print(myList)

print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)

del myList[0]
print(myList)

(54).__add__(21)
range(0, 10)
list(range(10))

range(5, 10)
list(range(5, 10))

list(range(5, 10, 2))
list(range(10, 1, -1)) # exclude 1

# strings 
myName = 'Peter'
myName.upper()
myName.find('P')
myName.split('t')

# my tuple
myTuple = (2, True, 4, 96)
myTuple[0]
myTuple[1] = False # error

# set 
mySet = {3,6,'cat', 4.5, False}
mySet
False in mySet

'dog' in mySet

yourSet = {99, 3, 100}
mySet.union(yourSet)

mySet | yourSet

mySet & yourSet

mySet - yourSet

{3}.issubset(mySet)
{3} >= mySet

mySet.pop()
mySet.clear()
mySet

# dictionary 
capitals = {'Iowa': 'DesMoines', 'Wisconsin':'Madison'}
print(capitals)
capitals['Utah'] = 'SaltLakeCity'
print(capitals) 

print(len(capitals))
for k in capitals:
    print(capitals[k], " is the capital of ", k)

phonetext = {'david':1410, 'brad':1137}
phonetext
phonetext.keys()
list(phonetext.keys())
phonetext.values()
list(phonetext.values())

phonetext.items()
list(phonetext.items())

phonetext.get('kent')
phonetext.get('kent', 'no entry')











