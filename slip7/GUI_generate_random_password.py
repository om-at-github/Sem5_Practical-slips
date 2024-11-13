# python GUI_generate_random_password.py

# Write python GUI program to generate a random password with upper and lower case letters

import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_click():
    password = generate_password(8)
    print("password",password)
    label_password.config(text=password)




root = tk.Tk()
root.title("generate passwords")

label_password = tk.Label(root, text="random password")
label_password.pack(pady=10)

button = tk.Button(root,command=on_generate_click,text="generate")
button.pack(pady=10)

root.mainloop()
