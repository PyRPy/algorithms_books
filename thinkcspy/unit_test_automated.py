# automated test
def round6(num: float) -> int:
    return int(num + 0.4) 

# the following is automated unit test  
result = round6(9.7)
assert result == 10 

result = round6(8.5) 
assert result == 8 

print("all tests passed!")