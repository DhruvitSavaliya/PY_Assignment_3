# Write a Python program to show multilevel inheritance.

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