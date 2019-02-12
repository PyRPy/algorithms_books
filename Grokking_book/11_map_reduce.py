# chpater 11 broad topics

# the map function
arr1 = [1, 2, 3, 4, 5]
arr2 = map(lambda x: 2*x, arr1 )

print("arr2 is: ", list(arr2)) # have to use list()

# the reduce function
import functools
arr3 = [1, 2, 3, 4, 5]
arr4 = functools.reduce(lambda x, y: x + y, arr3)

print("arr4 is reduced to: ", arr4)

# some examples from list comprehensions
# from Python pocket reference page 50
# the following two are equivalent
[x ** 2 for x in range(5)]

list(map((lambda x: x**2), range(5))) # map has atleast two arguments

# the following two are equivalent
[x for x in range(5) if x%2 == 0]

list(filter((lambda x: x % 2 == 0), range(5)))

# two equivalents
[x + y for x in range(3) for y in [10, 20, 30]]

res = []
for x in range(3):
    for y in [10, 20, 30]:
        res.append(x + y)
        
res
