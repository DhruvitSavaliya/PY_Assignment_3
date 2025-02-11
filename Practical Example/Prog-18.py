# Write a Python program to demonstrate the use of super() in inheritance. 

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
        parent_sound = super().speak()
        return f"{parent_sound} Specifically, {self.name}, the {self.breed}, barks."

dog = Dog("Buddy", "Golden Retriever")

print(dog.speak())

