# cd slip14

# python GUI_surface_area_and_volume_of_cylinder.py

# Write a Python GUI program to accept dimensions of a cylinder and display the 
# surface area and volume of cylinder. 

import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askfloat
import math

def cylinder():
    try:    
        r = rad.get()
        h = heh.get()
        surface_area = 2 * 3.14 * r * (r + h)
        volume = 3.14 * r * 2 * h
        messagebox.showinfo("Surface area = ",surface_area)
        messagebox.showinfo("Volume = ",volume)
                         
    except ValueError:
        messagebox.showerror("Error", "Invalid input")
    
        
root = tk.Tk()
rad = tk.IntVar()
heh = tk.IntVar()
r = tk.Entry(root,textvariable=rad)
h = tk.Entry(root,textvariable=heh)
B = tk.Button(root,text="calculate" ,command=cylinder)
r.pack(pady=10)
h.pack(pady=10)
B.pack(pady=20)
root.mainloop()