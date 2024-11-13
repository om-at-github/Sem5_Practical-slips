# cd slip24

# GUI_num_display_into_words.py

# Write  Python  GUI  program  which  accepts  a  number  n  to  displays  each  digit  of number in words. 


import tkinter as tk
from tkinter import messagebox

# Function to convert digits to words
def digit_to_word(digit):
    words = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three',
        '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
        '8': 'Eight', '9': 'Nine'
    }
    return words.get(digit, '')

# Function to handle button click event
def convert_number():
    number = entry.get()
    
    # Validate input (must be numeric)
    if not number.isdigit():
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return
    
    # Convert each digit to word
    word_representation = ' '.join(digit_to_word(digit) for digit in number)
    
    # Display the result
    result_label.config(text=f"Number in words: {word_representation}")

# Set up the main application window
root = tk.Tk()
root.title("Digit to Words Converter")

# Create and place the widgets
tk.Label(root, text="Enter a number:").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=convert_number)
convert_button.pack(pady=5)

result_label = tk.Label(root, text="Number in words will appear here.")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
