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

# 1.4. Calculating pi
def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

calculate_pi(10) 
calculate_pi(100)
calculate_pi(1000)

# 1.5. The Towers of Hanoi
from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):
    
    def __init__(self) -> None:
        self._container: List[T] = []
        
    def push(self, item: T) -> None:
        self._container.append(item)
        
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)
    
num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i) 

# 1.5.2. Solving The Towers of Hanoi
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
































