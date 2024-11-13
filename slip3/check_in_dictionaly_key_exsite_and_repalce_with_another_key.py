"""
cd slip3
python check_in_dictionaly_key_exsite_and_repalce_with_another_key.py
-Write a Python program to check if a given key already exists in a dictionary. If 
-key exists replace with another key/value pair
"""


my_dict={'key1':'value1','key2':'value2','key3':'value3'}
key=input("enter the key - ")
if key in my_dict:
    print("key exists in the dict :-")
    newkey = input("enter the new key - ")
    my_dict[newkey]=my_dict[key]
    del my_dict[key]
    print(my_dict)
else:
    print("key does not exist in the dict")

