#Write Python programs to demonstrate different types of inheritance 
# (single, multiple,multilevel, etc.).

#Single....

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name," makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed
    
    def speak(self):
        return f"{self.name}, the {self.breed}, barks."

generic_animal = Animal("Some Animal")
print(generic_animal.speak())  

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak()) 

#multiple..

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

#multilevel...

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name," makes a sound."
    
class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def describe(self):
        return self.name," is a mammal with",self.fur_color," fur."
    
class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def speak(self):
        return self.name," the ",self.breed," barks."

dog = Dog("Buddy", "golden", "Golden Retriever")

print(dog.describe())  
print(dog.speak())  