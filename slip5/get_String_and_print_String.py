## python get_String_and_print_String.py

## Write a Python script using class, which has two methods get_String and 
## print_String. get_String accept a string from the user and print_String print the 
## string in upper case


class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Enter a string: ")

    def print_String(self):
        print("Original String:", self.input_string)
        print("Uppercase String:", self.input_string.upper())

# Creating an instance of StringManipulator class
string_manipulator = StringManipulator()

# Getting input string from user
string_manipulator.get_String()

# Printing the string in uppercase
string_manipulator.print_String()
