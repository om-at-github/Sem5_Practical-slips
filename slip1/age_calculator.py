# Write Python GUI program to take accept your birthdate and output your age when a button is pressed.
# cd slip1
# python age_calculator.py

  
# Method: 1 Without using GUI
from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Input: Accept birthday as YYYY-MM-DD
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

# Calculate and print the age
age = calculate_age(birthdate)
print(f"You are {age} years old.")


## Method:2 Using GUI       ####################################################
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
   
    birthdate_str = entry.get()
    try:
    
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        
        messagebox.showinfo("Your Age", f"You are {age} years old.")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")


root = tk.Tk()
root.title("Age Calculator")

label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Calculate Age", command=calculate_age)
button.pack(pady=20)

root.mainloop()