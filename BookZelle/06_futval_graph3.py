# 06_futval_graph2.py
# further improvement on functions
from graphics import *

def drawBar(window, year, height):
    # draw bar for initial principal
    bar = Rectangle(Point(year,0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    # intro
    print("plot the growth of investment")

    # get principal and inerest rate
    principal = float(input("enter the initial principal: "))
    apr = float(input("enter the annualized interest rate: "))

    # create graph
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0), ' 0.0K').draw(win)
    Text(Point(-1,2500), ' 2.5K').draw(win)
    Text(Point(-1,5000), ' 5.0K').draw(win)
    Text(Point(-1,7500), ' 7.5K').draw(win)
    Text(Point(-1,10000), ' 10.0K').draw(win)

    drawBar(win, 0, principal)

    # draw a bar for each following year

    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)

    input("press <enter> to quit.")
    win.close()

main()
