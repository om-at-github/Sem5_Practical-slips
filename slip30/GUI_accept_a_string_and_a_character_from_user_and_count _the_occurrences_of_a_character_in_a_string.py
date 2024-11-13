# slip30

# python GUI_accept_a_string_and_a_character_from_user_and_count _the_occurrences_of_a_character_in_a_string.py

# Write a Python GUI program to accept a string and a character from user and count 
# the occurrences of a character in a string. 

import tkinter as tk
from tkinter import messagebox

def count_character_occurrences():
    # Get the input values from the user
    input_string = entry_string.get()
    input_char = entry_char.get()
     
    # Validate inputs
    if len(input_char) != 1:
        messagebox.showerror("Input Error", "Please enter exactly one character.")
        return
    
    # Count occurrences of the character
    count = input_string.count(input_char)
    
    # Display the result
    result_label.config(text=f"The character '{input_char}' appears {count} times.")

# Create the main window
root = tk.Tk()
root.title("Character Occurrence Counter")

# Create and place the widgets
tk.Label(root, text="Enter the string:").grid(row=0, column=0, padx=10, pady=5)
entry_string = tk.Entry(root, width=50)
entry_string.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the character:").grid(row=1, column=0, padx=10, pady=5)
entry_char = tk.Entry(root, width=5)
entry_char.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Count Occurrences", command=count_character_occurrences).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Run the application
root.mainloop()