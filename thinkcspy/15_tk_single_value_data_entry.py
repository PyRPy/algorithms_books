# 15_single_value_data_entry.py
import tkinter as tk   
from tkinter import simpledialog 
application_window = tk.Tk() 
answer = simpledialog.askstring("Input", "what is your first name?",
                                parent = application_window)
if answer is not None: 
    print("your first name is ", answer) 
else: 
    print("you don't have a first name?")

answer = simpledialog.askinteger("Input", "what is your age?",
                                parent = application_window, 
                                minvalue = 0, maxvalue = 100) 
if answer is not None: 
    print("your age is ", answer) 
else: 
    print("you don't have an age?")

answer = simpledialog.askfloat("Input", "what is your salary?", 
                                parent = application_window, 
                                minvalue = 0.0, maxvalue = 100000.0) 
if answer is not None: 
    print("your salary is ", answer) 
else:
    print("you don't have a salary?")
