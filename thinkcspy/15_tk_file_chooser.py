# 15_tk_file_chooser.py 
import tkinter as tk   
from tkinter import filedialog  
import os  

win = tk.Tk() 
my_filetypes = [('all files', '.*'), ('text files', '.txt')] 

# answer = filedialog.askdirectory(parent = win, 
#                                 initialdir = os.getcwd(),    
#                                 title = "please select a folder:")

answer = filedialog.askopenfilename(parent=win,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)

# answer = filedialog.askopenfilenames(parent=win,
#                                      initialdir=os.getcwd(),
#                                      title="Please select one or more files:",
#                                      filetypes=my_filetypes)

# answer = filedialog.asksaveasfilename(parent=win,
#                                       initialdir=os.getcwd(),
#                                       title="Please select a file name for saving:",
#                                       filetypes=my_filetypes)
