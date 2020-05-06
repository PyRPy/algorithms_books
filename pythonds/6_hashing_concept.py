# 6_hashing_concept.py
def hash(astring, tablesize):
    sum = 0 
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) 
    return sum % tablesize 

tablesize = 5
print(hash('cat', tablesize))
print(hash('dog', tablesize))
print(hash('pig', tablesize)) # same as 'cat' now
