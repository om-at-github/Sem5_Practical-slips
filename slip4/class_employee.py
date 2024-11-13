""" python class_employee.py

 Define a class Employee having members id, name, department, salary. Create a 
 subclass called manager with member bonus. Define methods accept and display in 
 both the classes. Create n objects of the manager class and display the details of the 
 manager having the maximum total salary (salary+bonus). 
"""

class Employee :
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        
    def acceptE(self):
        self.id = input("Enter ID: ")
        self.name = input("Enter Name: ")
        self.department = input("Enter Department: ")
        self.salary = float(input("Enter Salary: "))
    def displayE(self):
        print("self.id :")
        print("Name: ")
        print("Department: {")
        print("Salary: ")


class manager(Employee) :
    def __init__(self, id, name, department, salary, bonus):
        Employee.__init__(self, id, name, department, salary)
        self.bonus = bonus
    
    def acceptM(self):
        self.bonus = input("Enter bonus: ")
    def displayM(self):
        print("bonus :")
        
    def total_salary(self):
        total_salary=self.salary + self.bonus
        return total_salary
    
    n = int(input("Enter the number of managers: "))
    manager = []

    for i in range(n):
        
        acceptM()

        
        