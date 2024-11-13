## cd slip8
## python methods_get_String_and_print_String.py

## Write a Python class which has two methods get_String and print_String. get_String 
## accept a string from the user and print_String print the string in upper case. Further 
## modify the program to reverse a string word by word and print it in lower case.

class StringModifier:
    def __init__(self):
        self.input_string = ""
    
    def get_String(self):
        self.input_string = input("Enter a string: ")
    
    def print_String(self):
        print("Original string in uppercase:", self.input_string.upper())
    
    def reverse_and_print_lower(self):
        # Split the string into words, reverse them, and join back into a single string
        words = self.input_string.split()
        reversed_string = ' '.join(reversed(words))
        # Print the reversed string in lower case
        print("Reversed string word by word in lower case:", reversed_string.lower())

# Example usage:
if __name__ == "__main__":
    modifier = StringModifier()
    modifier.get_String()
    modifier.print_String()
    modifier.reverse_and_print_lower()
