# 15_tk_whack_a_mole_v1.py 
import tkinter as tk

def main():
    program = WhackAMole() 
    program.window.mainloop() 

class WhackAMole:
    def __init__(self): 
        self.window = tk.Tk() 
        self.mole_frame, self.status_frame = self.create_frames() 

    def create_frames(self): 
        mole_frame = tk.Frame(self.window, bg = 'red', width = 300, height = 300) 
        mole_frame.grid(row=1, column=1) 

        status_frame = tk.Frame(self.window, bg='green', width=100, height=300) 
        status_frame.grid(row=1, column=2) 

        return mole_frame, status_frame 

if __name__ == "__main__":
    main() 
