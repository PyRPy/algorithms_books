# greatest common divisor
def gcd(m, n):
    while m % n != 0:
        oldm = m 
        oldn = n 

        m = oldn 
        n = oldm % oldn 

    return n 

print(gcd(12, 18))