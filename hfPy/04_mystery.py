# chapter 4 code reuse 

def double(arg):
    print('before: ', arg)
    arg = arg * 2
    print('after: ', arg) 

def change(arg: list):
    print('before: ', arg) 
    arg.append('more data')
    print('after: ', arg) 

# test 

double(5)

change(['a', 'b', 'c'])