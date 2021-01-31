# code is based on :
# https://nptel.ac.in/courses/106/106/106106145/
# modification of the code is for educational purpose
# naive gcd and with one list
def gcd(m, n):
    
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            mrcf = i  # most recent common factor

    return mrcf

def gcd2(m, n):
    i = min(m, n)
    while i > 0:
        if m % i == 0 and n % i == 0:
            return i 
        else:
            i = i - 1

# try an example: find gcd between 14 and 63
m = 105
n = 35

print('method 1 : without a list: ')
print('greatest common divider between {} and {} is: {}\n'.format(m, n, gcd(m, n)))

print('method 2 : without a list and from large to small: ')
print('greatest common divider between {} and {} is: {}'.format(m, n, gcd2(m, n)))
