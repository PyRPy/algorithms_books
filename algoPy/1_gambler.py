# 1_gambler.py
import sys 
import random 
import time

# Accept integer command-line arguments stake, goal, and trialCount.
# Run trialCount experiments that start with stake dollars and
# terminate on 0 dollars or goal.  Write to standard output the
# percentage of wins and the average number of bets per experiment.

stake = int(sys.argv[1]) 
goal = int(sys.argv[2]) 
trials = int(sys.argv[3]) 

bets = 0 
wins = 0 
start = time.time()
for t in range(trials):
    cash = stake 
    while cash > 0 and cash < goal:
        bets += 1 
        if random.randrange(0, 2) == 0:
            cash += 1 
        else:
            cash -= 1 
    if cash == goal:
        wins += 1
end = time.time()
print(str(100 * wins // trials) + '% wins')
print('avg # bets: ' + str(bets//trials)) 
print('it takes ' + str(end - start) + ' seconds')
# python 1_gambler.py 10 100 1000
