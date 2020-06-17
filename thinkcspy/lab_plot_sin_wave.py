# plot a sin() wave
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(0, -1.5, 360, 1.5)
fred = turtle.Turtle()

#your code here
for angle in range(360):
    y = math.sin(math.radians(angle))
    fred.goto(angle, y)

wn.exitonclick()

# ref : https://stackoverflow.com/questions/20918749/how-to-draw-sine-in-python-turtle
# ref : https://runestone.academy/runestone/books/published/thinkcspy/Labs/sinlab.html