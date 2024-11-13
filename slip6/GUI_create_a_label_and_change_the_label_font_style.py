# cd slip6

# GUI_create_a_label_and_change_the_label_font_style.py

# Write  a  Python  GUI  program  to  create  a  label  and  change  the  label  font  style  (font 
# name, bold, size). Specify separate check button for each style.

import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter import Checkbutton



def changefont(font,weight,size):
    label.config(font=(font, size, "bold" if weight else "normal"))

def toggle_font(font,weight,size,varname):
    if varname:
        if varname.get():
            changefont(font,weight,size)
        else:
            changefont("Helvetica", False, 10)

root = tk.Tk()
label = tk.Label(root, text="omkar paygude")
label.pack(pady=20)


Checkbutton_var1 = tk.BooleanVar()
Checkbutton_var2 = tk.BooleanVar()
Checkbutton_var3 = tk.BooleanVar()
Checkbutton_var4 = tk.BooleanVar()

Checkbutton = tk.Checkbutton(root, text="Arial Bold 12", variable=Checkbutton_var1,command=lambda:toggle_font("Arial",True,12,Checkbutton_var1))
Checkbutton.pack(pady=20)
Checkbutton = tk.Checkbutton(root, text="Aptos Bold 24", variable=Checkbutton_var2,command=lambda:toggle_font("Aptos",True,24,Checkbutton_var2))
Checkbutton.pack(pady=20)
Checkbutton = tk.Checkbutton(root, text="Agency FB Bold 28", variable=Checkbutton_var3,command=lambda:toggle_font("Agency FB",True,28,Checkbutton_var3))
Checkbutton.pack(pady=20)
Checkbutton = tk.Checkbutton(root, text="Blackadder ITC Bold 30", variable=Checkbutton_var4,command=lambda:toggle_font("Blackadder ITC",True,30,Checkbutton_var4))
Checkbutton.pack(pady=20)

root.mainloop()