# basic animation
# step 1
from tkinter import *
import time

gui = Tk()
gui.geometry("800x600")
gui.title("Pi animation")
canvas = Canvas(gui,
                width = 800,
                height = 600,
                bg = "white",
                )

canvas.pack()

ball1 = canvas.create_oval(5,5,60,60, fill = "red")

# step 2
a = 5
b = 5
for x in range(0, 100):
    canvas.move(ball1, a, b)
    gui.update()
    time.sleep(0.01)

gui.mainloop()
