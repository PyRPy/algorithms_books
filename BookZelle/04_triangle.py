# 04_triangle.py
from graphics import * 

def main():
    win = GraphWin("Draw a triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5,0.5), "Click on three points")
    message.draw(win) 

    # draw three points 
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win) 

    # draw triangle using polygons 
    triangle = Polygon(p1, p2, p3) 
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win) 

    # wait for another click to exit 
    message.setText("click anywhere to quit.")
    win.getMouse()

main()