"""""
cd slip 12

python count_repeated_characters_string.py

Write a python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output: o-4, e-3, u-2, h-2, r-2, t-2

"""

characters = input("enter the string :-")
count_dict = {}
for char in characters:
    if char in count_dict:
        count_dict[char] += 1
        print("repeated characters in a string:-",count_dict)
    else:
        count_dict[char] = 1
        