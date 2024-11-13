# cd slip16

# python GUI_add_items_in_listbox_widget.py

# Write Python GUI program to add items in listbox widget and to print and delete the 
# selected items from listbox on button click. Provide three separate buttons to add, print 
# and delete.

import tkinter as tk
from tkinter import messagebox
import random

import tkinter as tk
from tkinter import messagebox

def show_selected_item():
    # Retrieve the selected item from the ListBox
    selected_item = listbox.get(tk.ACTIVE)
    # Display the selected item in a message box
    messagebox.showinfo("Selected Item", f"You selected: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("ListBox Example")

# Create a ListBox widget
listbox = tk.Listbox(root)
listbox.pack(padx=20, pady=20)

# Add items to the ListBox
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for item in items:
    listbox.insert(tk.END, item)

# Create a Button widget to show the selected item
button = tk.Button(root, text="Show Selected Item", command=show_selected_item)
button.pack(pady=10)

# Run the application
root.mainloop()

