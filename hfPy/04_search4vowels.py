# chapter 4 code reuse 
# functions and modules
def search4vowels(phrase: str) -> set:
    """returns the set of vowels found in 'phrase'.""" 
    return set('aeiou').intersection(set(phrase)) 

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ returns the set of 'letters' found in 'phrase'.""" 
    return set(letters).intersection(set(phrase)) 

# test 
print('search for vowels: ', search4vowels('hello'))

print('search for letters: ', search4letters('menotyou', 'mnst'))