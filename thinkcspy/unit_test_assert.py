# use assert 

def sumnums(low, high):
    """ return the sum of the numbers in the range(low, high)
        Precondition: low <= high
    """
    assert low <= high 

    sum = 0 
    for i in range(low, high+1):
        sum += i 
    return sum 

print(sumnums(1, 3))
print(sumnums(3, 1))
    