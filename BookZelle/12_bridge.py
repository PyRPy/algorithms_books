# 12_bridge.py
# simple program to deal and display bridge hands 

from random import randrange 

# constants for defining card rank values (int 2-14)
RANKS = list(range(2, 15)) 
RANKCHARS = "??23456789TJQKA" 

# constants for defining card suit values (int 0-3) 
SUITS = list(range(4)) 
SUITCHARS = "CDHS" 

class Card:
    # card objects have a rank (2-14) and a suit (0-3) 

    def __init__(self, rank, suit):
        self.suit = suit 
        self.rank = rank 

    def getRank(self):
        # returns: the rank of the card 
        return self.rank 

    def getSuit(self):
        # returns: the suit of the card 
        return self.suit

    def __str__(self):
        # a card is a string represented as "<rank> of <suit>"
        # where <rank> and <suit> are single characters
        return RANKCHARS[self.rank] + " of " + SUITCHARS[self.suit] 


class Hand:
    # a hand is a collection of cards representing a bridge hand 

    def __init__(self):
        # create an empty hand 
        self.cards = [] 

    def size(self):
        # return the number of cars in the hand
        return len(self.cards) 

    def addCard(self, card):
        # adds card to the hand 
        self.cards.append(card) 

    def countSuit(self, suit):
        # returns the count of cards in hand of the specified suit
        count = 0 
        for card in self.cards:
            if card.getSuit() == suit:
                count = count + 1 
        return count 

    def countRank(self, rank):
        # returns the count of cards in hand of the specified rank 
        count = 0 
        for card in self.cards:
            if card.getRank() == rank:
                count = count + 1 
        return count 

    def points(self):
        # returns: the number of 'points' a hand has. this is the sum
        # of the 'rank points' and 'suit pionts' for the hand 

        points = 0 
        for suit in SUITS:
            count = self.countSuit(suit) 
            if count < 3:
                points = points + (3- count) 

        for rank in range(11, 15):
            count = self.countRank(rank)
            points = points + count * (rank - 10) 
        return points 
        
    def biddableSuit(self):
        # returns: a Boolean indicating whether the hand contains a 
        # "biddable suit." 
        for suit in SUITS:
            count = self.countSuit(suit)
            if count > 4 or (count == 4 and self.suitHasHonor(suit)):
                return True 
        return False 
    
    def suitHasHonor(self, suit):
        # returns: a Boolean indicating whether the hand contains a face
        # card in the specified suit
        for card in self.cards:
            if card.getSuit() == suit and card.getRank() > 10:
                return True 
        return False  

    def canOpen(self):
        # returns: a Boolean indicating whether the hand is strong enough
        # to open
        return self.points() >= 13 and self.biddableSuit()  

    def sort(self):
        # sorts the cards in the hand 
        self.cards.sort(key = Card.getRank)
        self.cards.sort(key = Card.getSuit) 

    def getCards(self):
        # returns : an array containing the cards from the hand 
        return self.cards  

    def show(self):
        # prints out the cards in the hand 
        for card in self.cards:
            print(card) 

def charToSuit(ch):
    # convert a character ('C', 'D', 'H', 'S') to the corresponding 
    # suit code 
    return list(SUITCHARS).index(ch)  

class Deck:
    # represents a standard "deck" of playing cards 

    def __init__(self, fileStr = ""):
        # if file is "" (or not provided) a random deck is produced 
        # 0/w, fileStr is used as the name of a file from which the 
        # cards in the deck are read 
        if fileStr != "":
            self.fromFile(fileStr)
        else:
            self.newDeck() 
            self.shuffle() 

    def newDeck(self):
        # puta all the cards back in the deck in the standard order 
        self.cards = [] 
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))  

    def shuffle(self):
        # randomizes the order of the cards in the deck
        n = self.size() 
        cards = self.cards 
        for i in range(n-2):
            pos = randrange(i, n)
            cards[i], cards[pos] = cards[pos], cards[i]  

    def fromFile(self, fileName):
        # initializes the deck with cards read from specified file 
        self.cards = [] 
        datafile = open(fileName, 'r') 
        while True:
            line = datafile.readline() 
            if not line: break  
            rankStr, suitStr = line.split() 
            rank = int(rankStr) 
            suit = charToSuit(suitChar) 
            self.cards.append(Card(rank, suit)) 

    def dump(self, fileStr):
        # write a deck out to a file, suitable for loading back in 
        file = open(fileStr, "w")
        temp = "%d, '%s'\n" 
        for card in self.cards:
            outStr = temp % (card.getRank(), SUITCHARS[card.getSuit()])
            file.write(outStr) 
        file.close()

    def dealCard(self):
        # removes a card from the top of the deck 
        # returns: the card that was removed 
        card = self.cards[0] 
        del self.cards[0] 
        return card

    def size(self):
        # returns the number of cards in the deck 
        return len(self.cards) 

def introduction():
    print("This program simulates dealing four bridge hands and calcuating")
    print("the points for each and whether the hand can open a bid or not")
    print()
    print("The deck of cards can be generated randomly, not read from a file.")
    print() 

def getDeck():
    choice = input('Press "r" for random deck, or "f" for file: ') 
    if choice[0] == 'r' or choice[0] == 'R':
        fileStr = "" 
    else:
        fileStr = input("enter file name: ")
    return Deck(fileStr) 
     

def main():
    introduction() 
    deck = getDeck()
    hands = [Hand(), Hand(), Hand(), Hand()]
    while deck.size() > 0:
        for hand in hands:
            hand.addCard(deck.dealCard()) 
    headings = ["North", "East", "South", "West"]
    print() 
    for i in range(4):
        hand = hands[i] 
        print(headings[i])
        print("------")
        hand.sort() 
        hand.show() 
        print() 
        print("Points", hand.points()) 
        if hand.canOpen():
            print("Can open")
        else:
            print("Can't open")
        input("\nPress <Enter>")

if __name__ == "__main__":
    main() 
