#Write a Python program to show multiple inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return "Name:",self.name," Age: ",self.age
    
class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def get_employee_details(self):
        return "Employee ID: ",self.employee_id ," Department: ",self.department

class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)
        self.team_size = team_size

    def get_manager_details(self):
        return f"{self.get_details()}, {self.get_employee_details()}, Team Size: {self.team_size}"

manager = Manager("Alice", 35, "M123", "IT", 10)

print(manager.get_manager_details())