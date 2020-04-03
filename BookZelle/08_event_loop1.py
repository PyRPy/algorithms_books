# 08_event_loop1.py 
from graphics import * 
def main():
    win = GraphWin("color window", 500, 500) 

    # event loop : handle key presses until user press "q" key 
    while True:
        key = win.getKey() 
        if key == "q":
            break 

        # process key input 
        if key == "r":
            win.setBackground("pink") 
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("lightgray")
        elif key == "b":
            win.setBackground("lightblue")

    # exit program 
    win.close() 

main() 
