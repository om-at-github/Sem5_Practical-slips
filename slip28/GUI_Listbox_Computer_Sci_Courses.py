# cd slip28

# python GUI_Listbox_Computer_Sci_Courses.py

# Write a Python GUI program to create a list of Computer Science Courses using 
# Tkinter module (use Listbox).


import tkinter as tk
from tkinter import messagebox

# Function to add a course to the listbox
def add_course():
    course = entry.get()
    if course:
        listbox.insert(tk.END, course)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a course name.")

# Function to display the selected course
def show_selected_course():
    try:
        selected_index = listbox.curselection()[0]
        selected_course = listbox.get(selected_index)
        messagebox.showinfo("Selected Course", f"You selected: {selected_course}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a course from the list.")

# Create the main application window
root = tk.Tk()
root.title("Computer Science Courses")

# Create a Listbox widget
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(padx=10, pady=10)

# Sample courses to display initially
sample_courses = [
    "Introduction to Programming",
    "Data Structures and Algorithms",
    "Computer Networks",
    "Operating Systems",
    "Database Systems",
    "Software Engineering"
]

# Add the sample courses to the Listbox
for course in sample_courses:
    listbox.insert(tk.END, course)

# Create an Entry widget to input new courses
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Create a button to add new courses
add_button = tk.Button(root, text="Add Course", command=add_course)
add_button.pack(padx=10, pady=5)

# Create a button to show the selected course
show_button = tk.Button(root, text="Show Selected Course", command=show_selected_course)
show_button.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()

"""
import tkinter as tk

# Function to handle listbox selection
def on_select(event):
    selected_item = listbox.get(listbox.curselection())
    label.config(text=f"Selected: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("Listbox Example")

# Create a Listbox widget
listbox = tk.Listbox(root)
listbox.pack(padx=20, pady=20)

# Add some items to the Listbox
items = [ "Introduction to Programming",
    "Data Structures and Algorithms",
    "Computer Networks",
    "Operating Systems",
    "Database Systems",
    "Software Engineering"
    ]
for item in items:
    listbox.insert(tk.END, item)

# Bind the listbox selection event to the handler function
listbox.bind("<<ListboxSelect>>", on_select)

# Create a Label widget to display the selected item
label = tk.Label(root, text="Selected: None")
label.pack(padx=20, pady=20)

# Start the main event loop
root.mainloop()

"""