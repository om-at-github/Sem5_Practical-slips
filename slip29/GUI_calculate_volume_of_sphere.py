# cd slip29

# python GUI_calculate_volume_of_sphere.py

# Write a Python GUI program to calculate volume of Sphere by accepting radius as input.
# volume = 4/3*3.14*r*r*r   

import tkinter as tk
from tkinter import messagebox
import math

def calculate_volume():
    try:
        radius = float(radius_entry.get())
        if radius < 0:
            messagebox.showerror("Input Error", "Radius must be a non-negative number.")
            return
        volume = (4/3) * math.pi * (radius ** 3)
        result_label.config(text=f"Volume of the Sphere: {volume:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Sphere Volume Calculator")


tk.Label(root, text="Enter Radius:").grid(row=0, column=0, padx=10, pady=10)

radius_entry = tk.Entry(root)
radius_entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Volume", command=calculate_volume)
calculate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Volume of the Sphere: ")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
