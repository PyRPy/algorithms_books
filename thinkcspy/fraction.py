# fraction in class
# https://runestone.academy/ns/books/published/thinkcspy/ClassesDiggingDeeper/Fractions.html

# greatest common divisor
def gcd(m, n):
    while m % n != 0:
        oldm = m 
        oldn = n 

        m = oldn 
        n = oldm % oldn 

    return n 

class Fraction:
    def __init__(self, top, bottom):
        self.num = top  
        self.den = bottom 

    def __str__(self):
        return str(self.num) + "/" + str(self.den) 

    def getNum(self):
        return self.num 

    def getDen(self):
        return self.den 

    def simplify(self): 
        common = gcd(self.num, self.den) 
        self.num = self.num // common 
        self.den = self.den // common 

    def add(self, otherFraction):
        newnum = self.num*otherFraction.den + self.den*otherFraction.num
        newden = self.den * otherFraction.den 

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __add__(self, otherfraction):
    
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)


myFraction = Fraction(12, 18) 
print(myFraction)

print(myFraction.getNum())
print(myFraction.getDen())

myFraction.simplify()
print(myFraction)

# sameness 'is' 
fraction1 = Fraction(3, 4)
fraction2 = Fraction(6, 8) 
print(fraction1 == fraction2) # False
print(fraction1 is fraction2) # False too ?

# fraction addition
fraction3 = fraction1.add(fraction2)
print(fraction3)