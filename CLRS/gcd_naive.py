# code is based on :
# https://nptel.ac.in/courses/106/106/106106145/
# modification of the code is for educational purpose
# naive gcd
def gcd(m, n):
    if m > n:
        m, n = n, m
    fm = []
    for i in range(1, m+1):
        if m % i == 0:
            fm.append(i)

    fn = []
    for j in range(1, n+1):
        if n % j == 0:
            fn.append(j)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return cf[-1]

# try an example: find gcd between 14 and 63
m = 63
n = 14

print('greatest common divider between {} and {} is: {}'.format(m, n, gcd(m, n)))
            
