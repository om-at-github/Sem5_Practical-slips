# cd slip23

# python GUI_ change_the_label_font_style_font_name_bold_size.py

# Write a Python GUI program to create a label and change the label font style (font 
# name, bold, size) using tkinter module

import tkinter as tk
import tkinter.font as tkfont
from tkinter import font

root = tk.Tk()
root.title("changer font of name")

label = tk.Label(root, text="Hello, world!")
label.pack(pady=20)

font = tkfont.Font(family="Arial", size=24, weight="bold")
label.config(font=font)

font1 = tkfont.Font(family="Arial", size=8, weight="bold")
label.config(font=font1)

root.mainloop()


"""
import tkinter as tk
from tkinter import font

def update_label():
    font_name = font_name_entry.get()
    font_size = font_size_entry.get()
    is_bold = bold_var.get()

    # Determine font style
    if is_bold:
        label_font = (font_name, int(font_size), 'bold')
    else:
        label_font = (font_name, int(font_size))
    
    label.config(font=label_font)

# Create the main window
root = tk.Tk()
root.title("Font Style Changer")

# Create a label
label = tk.Label(root, text="Sample Text", font=("Arial", 12))
label.pack(pady=20)

# Create entry fields for font name and size
font_name_label = tk.Label(root, text="Font Name:")
font_name_label.pack()
font_name_entry = tk.Entry(root)
font_name_entry.pack()
font_name_entry.insert(0,"Blackadder ITC")
font_name_entry.insert(0,"Aptos,Bradley Hand ITC")
font_name_entry.insert(0, "Arial")  # Default font name

font_size_label = tk.Label(root, text="Font Size:")
font_size_label.pack()
font_size_entry = tk.Entry(root)
font_size_entry.pack()
font_size_entry.insert(0, "12")  # Default font size

# Create a checkbox for bold
bold_var = tk.BooleanVar()
bold_checkbutton = tk.Checkbutton(root, text="Bold", variable=bold_var)
bold_checkbutton.pack()

# Create an update button
update_button = tk.Button(root, text="Update Font", command=update_label)
update_button.pack(pady=10)

# Run the application
root.mainloop()
"""