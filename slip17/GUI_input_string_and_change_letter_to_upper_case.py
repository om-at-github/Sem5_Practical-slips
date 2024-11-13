# cd slip17

# python GUI_input_string_and_change_letter_to_upper_case.py

# Write Python GUI program that takes input string and change letter to upper case 
# when a button is pressed. 

from tkinter.simpledialog import askstring
from tkinter import *
from tkinter import ttk

def convert_to_uppercase():
    try:
        global Strings
        Strings = Strings.upper()
        print(Strings)
    except:
        return "Error"
        
root = Tk()
root.title("String to Upper Case")
root.geometry("300x200")

convert_button = ttk.Button(root, text="Convert to Uppercase" ,command=convert_to_uppercase)
convert_button.pack(padx=10, pady=5)

root.mainloop()