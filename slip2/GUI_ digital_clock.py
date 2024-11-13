# GUI_ digital clock.py

# Write Python GUI program to create a digital clock with Tkinter to display the time.

import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, clock)


root = tk.Tk()
root.title("digital clock")
clock_label = tk.Label(root, text="time")
clock_label.pack(pady=10)
clock()

root.mainloop()