## cd slip9
## python reverse_string_word_to_word.py
## Write a Python script using class to reverse a string word by word


class StringReverser:
    def reverse_words(self, input_string):
        # Split the input string into words
        words = input_string.split()

        # Reverse the list of words
        reversed_words = words[::-1]

        # Join the reversed words into a single string
        reversed_string = ' '.join(reversed_words)

        return reversed_string

# Example usage:
if __name__ == "__main__":
    # Create an instance of StringReverser
    reverser = StringReverser()

    # Input string
    input_string = "Hello World, how are you?"

    # Reverse the string word by word
    reversed_string = reverser.reverse_words(input_string)

    # Print the reversed string
    print("Original String:", input_string)
    print("Reversed String:", reversed_string)
