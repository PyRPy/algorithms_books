# dieview2.py
# use list of objects
from graphics import * 
class DieView:
    """ DieView is a widget that displays a graphical representation
    of a stanard six-sided die.""" 

    def __init__(self, win, center, size): 
        """Create a view of a die, e.g.:
        d1 = DieView(myWin, Point(40, 50), 20) 
        creates a die centered at (40,50) having sides 
        of length 20.""" 

        # first define some standard values 
        self.win = win              # save this for drawing pips later 
        self.background = "white"   # color of die face 
        self.foreground = "black"   # color fo the pips 
        self.psize = 0.1 * size     # radius of each pip 
        hsize = size / 2.0          # half the size of the die 
        offset = 0.6 * hsize        # distance from center to outer pips 

        # create a square for the face 
        cx, cy = center.getX(), center.getY() 
        p1 = Point(cx - hsize, cy - hsize) 
        p2 = Point(cx + hsize, cy + hsize) 
        rect = Rectangle(p1, p2) 
        rect.draw(win)
        rect.setFill(self.background) 

        # create 7 circles for standard pip locations
        self.pips = [ self.__makePip(cx - offset, cy - offset), 
                      self.__makePip(cx - offset, cy),
                      self.__makePip(cx - offset, cy + offset),
                      self.__makePip(cx, cy),
                      self.__makePip(cx + offset, cy - offset),
                      self.__makePip(cx + offset, cy),
                      self.__makePip(cx + offset, cy + offset)]

        # create a table for which pips are on for each value 
        # draw an initial value 
        self.OnTable = [[], [3], [2,4], [2,3,4], [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6]] 
        self.setValue(1) 

    def __makePip(self, x, y):
        """Internal helper method to draw a pip at (x,y).""" 
        pip = Circle(Point(x,y), self.psize) 
        pip.setFill(self.background) 
        pip.setOutline(self.background) 
        pip.draw(self.win) 
        return pip 

    def setValue(self, value):
        """Set this die to display value.""" 
        # turn all pips off 
        for pip in self.pips:
            pip.setFill(self.background) 
        
        # turn correct pips on 
        for i in self.OnTable[value]:
            self.pips[i].setFill(self.foreground)
