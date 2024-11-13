## python GUI_accept_brithdate_and_output_your_age.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_year = int(entry_year.get())
        current_year = datetime.now().year
        age = current_year - birth_year
        messagebox.showinfo("Age", f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid year.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")

# Create a label and entry for birth year
label_year = tk.Label(root, text="Enter your birth year:")
label_year.pack(pady=10)

entry_year = tk.Entry(root)
entry_year.pack(pady=10)

# Create a button to calculate age
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()