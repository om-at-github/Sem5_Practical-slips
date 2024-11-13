## python accepts_a_string_and_calculate_the_number_of_upper_case_letters_and_lower_case_letters.py

## Write a Python function that accepts a string and calculate the number of upper case 
## letters and lower case letters.  
## Sample String: 'The quick Brown Fox'
## Expected Output:   
## No. of Upper case characters: 3
## No. of Lower case characters: 13

def count_case_characters(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper(): 
            upper_count += 1
        elif char.islower():
            lower_count += 1
 
    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)

# Example usage:
sample_string = input("enter the string:")
count_case_characters(sample_string)