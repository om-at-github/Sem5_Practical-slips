# cd slip11

# python GUI_add_menu_bar_with_name_of_colors_as_options_to _change_the_background_color.py

# Write Python GUI program to add menu bar with name of colors as options to 
# change the background color as per selection from menu option. 

import tkinter as tk
from tkinter import Menu

# Function to change background color
def change_bg_color(color):
    root.configure(bg=color)

# Create the main window
root = tk.Tk()
root.title("Background Color Changer")
root.geometry("300x200")

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a menu for colors
color_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Colors", menu=color_menu)

# Add color options to the menu
colors = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta", "White", "Black"]

for color in colors:
    color_menu.add_command(label=color, command=lambda c=color: change_bg_color(c.lower()))

# Start the Tkinter event loop
root.mainloop()

"""
import tkinter as tk
from tkinter import Menu

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'white']

def change_color():
    color = Menu.choice(colors)
    root.config(bg=color)
    root.after(1000,change_color)

root = tk.Tk()
root.geometry("200x200")
root.title("Color Changer")

menu_bar = Menu(root)
root.config(menu=menu_bar)

for color in colors:
    Menu.add_command(label=color, command=lambda c=color.lower(): change_color(c))

button = tk.Button(root, text="Change Color", command=change_color, font=('Arial', 16))
button.pack(pady=20)
change_color()

root.mainloop()
"""