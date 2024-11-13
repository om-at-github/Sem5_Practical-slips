"""
cd slip13
python exceptionHandling.py

Write a Python program to input a positive integer. Display correct message for 
correct and incorrect input. (Use Exception Handling)

"""
class invalidnumber(Exception):
    pass

number = int(input("enter the number :"))

try:
    if number < 0:
        raise invalidnumber

except:
    print("number is negative")

"""""
while True:
try:
    number=int(input("enter the number :"))
    if(number>0):
        break
    else:
        print("num not positive")

    except ValueError:
        print("input must be integer")        
"""