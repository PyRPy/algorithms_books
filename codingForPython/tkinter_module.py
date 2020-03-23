# tkinter_module.py
from tkinter import *
import tkinter as tk 
wind = Tk()
btn = Button()
btn.pack()
btn["text"] = "hello"

def click():
    print("you cliked me")

btn["command"] = click
