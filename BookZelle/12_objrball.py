# 09_rball.py
# 12_objrball.py
# modified into oop or ood

from random import random 

class Player:
    # A player keep track of service probability and score

    def __init__(self, prob):
        # create a player with this probability
        self.prob = prob 
        self.score = 0 

    def winsServe(self):
        # returns a Boolean that is true with probability self.prob
        return random() < self.prob 

    def incScore(self):
        # add a point to this player's score 
        self.score = self.score + 1 
    
    def getScore(self):
        # returns this player's current score 
        return self.score 

class RBallGame:
    # a RBallGame represents a game in progress. A game has two players
    # and keeps track of which one is currently serving 

    def __init__(self, probA, probB):
        # create a new game having players with the given probs 
        self.playerA = Player(probA) 
        self.playerB = Player(probB)
        self.server = self.playerA # player A always serves first 
    
    def play(self):
        # play the game to completion 
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore() 
            else:
                self.changeServer() 

    def isOver(self):
        # return game is finished (i.e. one of the players has won)
        a, b = self.getScores() 
        return a == 15 or b == 15 or \
            (a == 7 and b == 0) or (b == 7 and a == 0) 

    def changeServer(self):
        # switch which player is serving 
        if self.server == self.playerA:
            self.server = self.playerB 
        else:
            self.server = self.playerA 

    def getScores(self):
        # return the current scores of player A and player B 
        return self.playerA.getScore(), self.playerB.getScore()

class SimStats:
    # SimStats handles accumulation of statistics across multiple
    # 'completed' games. This version tracks the wins and shutouts for
    # each player 

    def __init__(self):
        # create a new accumulator for a series of games 
        self.winsA = 0 
        self.winsB = 0 
        self.shutsA = 0 
        self.shutsB = 0 

    def update(self, aGame):
        # determine the outcome of aGame and updates stats 
        a, b = aGame.getScores() 
        if a > b:
            self.winsA = self.winsA + 1 
            if b == 0:
                self.shutsA = self.shutsA +  1 
        else:
            self.winsB = self.winsB + 1 
            if a == 0:
                self.shutsB = self.shutsB + 1 

    def printReport(self):
        # print a nicely formatted report 
        n = self.winsA + self.winsB 
        print("summary of", n, "games:\n")
        print("           wins (% total)    shutouts (% wins)  ")
        print("-----------------------------------------")
        self.printLine("A", self.winsA, self.shutsA, n)
        self.printLine("B", self.winsB, self.shutsB, n) 

    def printLine(self, label, wins, shuts, n):
        template = "Player {0}:{1:5}  ({2:5.1%}) {3:11}   ({4})"
        if wins == 0:
            shutStr = "------"
        else:
            shutStr = "{0:4.1%}".format(float(shuts)/wins) 
        print(template.format(label, wins, float(wins)/n, shuts, shutStr)) 



def printIntro():
    print("this program simuates a game of racquetball between two")
    print("players call 'A' and 'B'. The ability of each player is")
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInputs():
    # returns the three simulation parameters probA, probB and n 
    a = float(input("what is the prob. player A wins a serve? ")) 
    b = float(input("what is the prob. player B wins a serve? "))
    n = int(input("how many games to simulate? "))
    return a, b, n 

def main():
    printIntro() 

    probA, probB, n = getInputs() 

    # play the games 
    stats = SimStats()
    for i in range(n):
        theGame = RBallGame(probA, probB)
        theGame.play()
        stats.update(theGame)

    # print the results 
    stats.printReport()


if __name__ == '__main__': 
    main() 
    input("\nPress <Enter> to quit>")
    