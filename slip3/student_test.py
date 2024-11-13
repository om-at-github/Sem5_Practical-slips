## python student_test.py

##  Write a python script to define a class student having members roll no, name, age, 
## gender. Create a subclass called Test with member marks of 3 subjects. Create three 
## objects of the Test class and display all the details of the student with total marks.

class Student:
    def __init__(self, roll_no, name, age, gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

class Test(Student):
    def __init__(self, roll_no, name, age, gender, marks_subject1, marks_subject2, marks_subject3):
        super().__init__(roll_no, name, age, gender)
        self.marks_subject1 = marks_subject1
        self.marks_subject2 = marks_subject2
        self.marks_subject3 = marks_subject3
    
    def display_details(self):
        total_marks = self.marks_subject1 + self.marks_subject2 + self.marks_subject3
        print(f"Student Details:")
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Marks in Subject 1: {self.marks_subject1}")
        print(f"Marks in Subject 2: {self.marks_subject2}")
        print(f"Marks in Subject 3: {self.marks_subject3}")
        print(f"Total Marks: {total_marks}")

# Creating three objects of the Test class
student1 = Test("A101", "Alice", 20, "Female", 85, 90, 88)
student2 = Test("B202", "Bob", 21, "Male", 78, 85, 90)
student3 = Test("C303", "Carol", 19, "Female", 92, 88, 85)

# Displaying details of each student with total marks
student1.display_details()
print("\n")
student2.display_details()
print("\n")
student3.display_details()
