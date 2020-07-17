# gfg_find_election_winner
from collections import Counter

def winner(input):
    votes = Counter(input)

    dict = {}
    for value in votes.values():
        dict[value] = []
    for (key, value) in votes.items():
        dict[value].append(key)

    maxVote = sorted(dict.keys(), reverse=True)[0]

    if len(dict[maxVote]) > 1:
        print(sorted(dict[maxVote])[0])
    else:
        print(dict[maxVote])[0]

# test
input = ['john','johnny','jackie','johnny','john','jackie','jamie','jamie', 
'john','johnny','jamie','johnny','john']

winner(input)

# method 2
vote_count = Counter(input)
max_votes = max(vote_count.values())
lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]
print(sorted(lst)[0])
# https://www.geeksforgeeks.org/dictionary-counter-python-find-winner-election/

