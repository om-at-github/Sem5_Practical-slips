# cd slip4
# GUI_create_background_with_changing_colors.py

# Write Python GUI program to create background with changing colors 

import tkinter as tk
import random

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'white']

def change_color():
    color = random.choice(colors)
    root.config(bg=color)
    root.after(1000,change_color) # 1000 means 1 second

root = tk.Tk()
root.geometry("200x200")
root.title("Color Changer")

#button = tk.Button(root, text="Change Color", command=change_color, font=('Arial', 16))
#button.pack(pady=20)
change_color()

root.mainloop()