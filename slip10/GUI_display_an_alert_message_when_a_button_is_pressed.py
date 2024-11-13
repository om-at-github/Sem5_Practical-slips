# cd slip10

# python GUI_display_an_alert_message_when_a_button_is_pressed.py

#  Write Python GUI program to display an alert message when a button is pressed .


import tkinter as tk
from tkinter import messagebox
def alert_message():
    
    messagebox.showinfo("Alert" , "x Alert")

root = tk.Tk()
root.title("alert message show")
B = tk.Button(root, text ="Click", command = alert_message)
B.pack(pady=20)

################################################################################################

# Function to be called when the button is pressed
def show_alert():
    messagebox.showinfo("Alert", "Button was pressed!")

# Create the main application window
root = tk.Tk()
root.title("Button Alert Example")

# Create a button and add it to the window
button = tk.Button(root, text="Press Me", command=show_alert)
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()