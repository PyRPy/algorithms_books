# gfg_shuffle_deck_of_cards.py
import random
def shuffle(card, n):
    for i in range(n):
        r = i + random.randint(0, 55) % (52 - i)  
        tmp = card[i] 
        card[i] = card[r] 
        card[r] = tmp 

# test 
if __name__ == '__main__':
    cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 
	        9, 10, 11, 12, 13, 14, 15, 
	        16, 17, 18, 19, 20, 21, 22, 
	        23, 24, 25, 26, 27, 28, 29, 
	        30, 31, 32, 33, 34, 35, 36, 
	        37, 38, 39, 40, 41, 42, 43, 
	        44, 45, 46, 47, 48, 49, 50, 
	        51] 

shuffle(cards, 52) 
print(cards) 
# https://www.geeksforgeeks.org/shuffle-a-deck-of-cards-3/
