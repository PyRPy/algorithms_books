# code is based on :
# https://nptel.ac.in/courses/106/106/106106145/
# modification of the code is for educational purpose
# use Euclid's method, not very friendly for beginners
# use recursion instead of loops
def gcd(m, n):
    if m < n:
        m, n = n, m 
    
    if m % n == 0:
        return n 

    else:
        diff = m - n 
        return gcd(max(n, diff), min(n, diff))

def gcd2(m, n):
    if m < n:
        m, n = n, m 
    while m % n != 0:
        diff = m - n 
        m, n = max(n, diff), min(n, diff)
    return n 

# try an example: find gcd between 14 and 63
m = 105
n = 35

print('Eudlic\'s method with recursion: ')
print('greatest common divider between {} and {} is: {}\n'.format(m, n, gcd(m, n)))

print('Eudlic\'s method with while loop: ')
print('greatest common divider between {} and {} is: {}'.format(m, n, gcd2(m, n)))