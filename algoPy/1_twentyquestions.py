# 1_twentyquestions.py
import random 

# Generate a random integer. Repeatedly read user guesses from
# standard input. Write 'Too low' or 'Too high' to standard output,
# as appropriate, in response to each guess. Write 'You win!' to
# standard output and exit when the user's guess is correct.

RANGE = 100 
secret = random.randrange(1, RANGE + 1) 
print('i am thinking of a secret number between 1 and ')
print(RANGE)
guess = 0 
while guess != secret:
    print('what is your guess? ')
    guess = int(input('enter a number: '))
    if guess < secret:
        print('too low')
    elif guess > secret:
        print('too high')
    else:
        print('you win!')
# https://introcs.cs.princeton.edu/python/15inout/twentyquestions.py.html
