# Chapter 1 Small problems
import sys
sys.setrecursionlimit(1500)
## 1.1. The Fibonacci sequence
# 1.1.1. A first recursive attempt
def fib1(n: int)-> int:
    return fib1(n-2) + fib1(n-1)

fib1(5)
# it's going to find 5, 4, 3, 2, until 1
if __name__ == "__main__":
    print(fib1(5))
    
# 1.1.2. Utilizing base cases    
def fib2(n: int) -> int:
    if n < 2:
        return n
    return fib2(n - 2) + fib2(n - 1)

fib2(5)
fib2(10)

# 1.1.3. Memoization to the rescue
from typing import Dict
memo: Dict[int, int] = {0:0, 1:1}

def fib3(n: int)-> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n - 2)
    return memo[n]
    
fib3(5)
fib3(20)
## basics are essential part of programming !

# 1.1.4. Automatic memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n - 2) + fib4(n - 1)

fib4(5)
fib4(20)

# 1.1.5. Keep it simple, Fibonacci
def fib5(n: int) -> int:
    if n == 0: return 0
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

fib5(5)

# 1.1.6. Generating Fibonacci numbers with a generator
from typing import Generator
def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next
        
fib5(5)
    