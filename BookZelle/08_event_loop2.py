# 08_event_loop1.py 
# more event and responses from keyboard
from graphics import * 

def handleKey(k, win):
    # process key input 
    if k == "r":
        win.setBackground("pink") 
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win):
    pass 

def main():
    win = GraphWin("color window", 500, 500) 

    # event loop : handle key presses and mouse clicks until 
    # user press "q" key 
    while True:
        key = win.getKey() 
        if key == "q":
            break 
        if key: 
            handleKey(key, win) 

        pt = win.checkMouse() 
        if pt:
            handleClick(pt, win) 
    
    # exit program 
    win.close() 

main() 