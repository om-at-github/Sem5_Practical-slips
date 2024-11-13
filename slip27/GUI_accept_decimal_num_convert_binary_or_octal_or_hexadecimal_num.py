# cd slip27

# python GUI_accept_decimal_num_convert_binary_or_octal_or_hexadecimal_num.py

# Write Python GUI program to accept a decimal number and convert and display it to 
# binary, octal(0 to 7) and hexadecimal(0 to 16) number.

import tkinter as tk
from tkinter import messagebox

# Function to convert the decimal number
def convert_number():
    try:
        # Get the decimal number from the entry box
        decimal_number = int(entry.get())
        
        # Convert to binary, octal, and hexadecimal
        binary_result = bin(decimal_number)[2:]
        octal_result = oct(decimal_number)[2:]
        hexadecimal_result = hex(decimal_number)[2:].upper()

        # Display the results
        binary_label.config(text=f"Binary: {binary_result}")
        octal_label.config(text=f"Octal: {octal_result}")
        hexadecimal_label.config(text=f"Hexadecimal: {hexadecimal_result}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Number Converter")

# Create and place widgets
tk.Label(root, text="Enter a decimal number:").grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_number)
convert_button.grid(row=0, column=2, padx=10, pady=10)

binary_label = tk.Label(root, text="Binary: ")
binary_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

octal_label = tk.Label(root, text="Octal: ")
octal_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

hexadecimal_label = tk.Label(root, text="Hexadecimal: ")
hexadecimal_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Start the main event loop
root.mainloop()