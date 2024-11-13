# cd slip9

# python GUI_it_is_Prime_Perfect_or_Armstrong_number_or_not.py

# Write Python GUI program to accept a number n and check whether it is Prime, 
# Perfect or Armstrong number or not. Specify three radio buttons. 

import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askinteger,askfloat,askstring
from tkinter import *

def prime_number():
    
        number = int(num.get())
        if number % 2==0:
            lb.config(text="it is even number")
        else:
           lb.config(text="it is not a even number")

root = tk.Tk()
root.title("check odd even")

num = tk.Entry(root)
num.pack(pady=10)

bt = tk.Button(text="Check",command=prime_number)
bt.pack(pady=10)
lb = tk.Label()
lb.pack(pady=10)

root.mainloop()