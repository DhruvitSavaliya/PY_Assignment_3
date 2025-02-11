# Write a Python program to show hierarchical inheritance. 

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name," makes a sound."

class Dog(Animal):
    def speak(self):
        return self.name," barks."

class Cat(Animal):
    def speak(self):
        return self.name," meows."

class Bird(Animal):
    def speak(self):
        return self.name," chirps."

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

print(dog.speak())  
print(cat.speak())   
print(bird.speak()) 
