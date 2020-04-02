# 06_addinterest1.py
def addInterest(balance, rate):
    newBalance = balance * (1 + rate)
    return newBalance 

def test():
    amount = 1000 
    rate = 0.05 
    amount = addInterest(amount, rate)
    print(amount)

test() # reference to page-195, fig-6.7


