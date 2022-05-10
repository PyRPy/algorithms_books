def round6(num: float) -> int:
    """This function has a bug in it"""
    return int(num + .6)

# ---- automated unit test ----

def test_round6():
    assert round6(9.7) == 10
    assert round6(8.5) == 8

# main program follows

if __name__ == "__main__":
    num = float(input('Enter a value:'))
    print('The value rounded is: ' + str(round6(num))) 
    