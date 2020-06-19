# 15_tk_color_chooser.py
from tkinter import colorchooser 
import tkinter as tk 
win = tk.Tk() 

rgb_color, web_color = colorchooser.askcolor(parent = win, 
                                            initialcolor = (250, 0, 0))
