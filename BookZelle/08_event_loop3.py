# 08_event_loop1.py 
# more event and responses from keyboard
# realize mouse clicks
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
    # create an entry for user to type in 
    entry = Entry(pt, 10) 
    entry.draw(win) 

    # go modal, loop until user types <Enter> key 
    while True:
        key = win.getKey() 
        if key == "Return": break 

    # undraw the entry and create and draw Text0 
    entry.undraw() 
    typed = entry.getText() 
    Text(pt, typed).draw(win) 

    win.checkMouse() 

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