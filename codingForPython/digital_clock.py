# digital_clock.py
import time 
import tkinter as tk 

def tick(time1=''):
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2 
        clock.config(text=time2)

    clock.after(200, tick)

root = tk.Tk()
clock = tk.Label(root, font=('arial', 20, 'bold'), bg='green')
clock.pack(fill='both', expand=1)
tick()
root.mainloop()