# Write a Python program to show single inheritance.

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
        return self.name," the ",self.breed," barks."

generic_animal = Animal("Some Animal")
print(generic_animal.speak())  

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.speak()) 