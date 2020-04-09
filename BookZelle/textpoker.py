# textpoker.py
from pokerapp import PokerApp

class TextInterface:

    def __init__(self):
        print("welcome to video poker.")

    def setMoney(self, amt):
        print("you currently have ${0}.".format(amt)) 

    def setDice(self, values):
        print("Dice:", values) 

    def wantToPlay(self):
        ans = input("do you wish to try your luck? ")
        return ans[0] in "yY" 

    def close(self):
        print("\nThanks for playing")
    
    def showResult(self, msg, score):
        print("{0}. You win ${1}.".format(msg, score))

    def chooseDice(self):
        return eval(input("enter list of which to change ([] to stop) "))

def main():
    inter = TextInterface()
    app = PokerApp(inter)
    app.run() 

if __name__ == "__main__":
    main()
