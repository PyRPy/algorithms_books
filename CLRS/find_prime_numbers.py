# find_prime_numbers.py
def isPrime(n):
    for num in range(2, n//2):
        if n % num == 0:
            return False 
    return True 

def kth_prime(k):
    candidate = 2
    while k:
        if isPrime(candidate):
            k -= 1
        candidate += 1 
    return candidate - 1 

# test code 
print(kth_prime(100)) 

# https://medium.com/delta-force/extending-python-with-c-f4e9656fbf5d
