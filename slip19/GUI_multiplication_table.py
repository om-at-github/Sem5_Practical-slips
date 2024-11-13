# cd slip19

# python GUI_multiplication_table.py

# Write  a  Python  GUI  program  to  accept  a  number form  user  and  display its 
# multiplication table on button click.


import tkinter as tk
from tkinter import messagebox

def generate_table():
    try:
        # Get the number from the entry widget
        number = int(number_entry.get())
        # Prepare the multiplication table
        table = ""
        for i in range(1, 11):
            table += f"{number} x {i} = {number * i}\n"
        # Display the table in the text area
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, table)
        result_text.config(state=tk.DISABLED)
    except ValueError:
        # Show an error message if input is not a valid integer
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main application window
root = tk.Tk()
root.title("Multiplication Table Generator")

# Create and place widgets in the window
tk.Label(root, text="Enter a number:").pack(pady=10)

number_entry = tk.Entry(root)
number_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Table", command=generate_table)
generate_button.pack(pady=10)

result_text = tk.Text(root, height=10, width=30, wrap=tk.WORD, state=tk.DISABLED)
result_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
