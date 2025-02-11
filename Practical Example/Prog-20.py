#Write a Python program to show method overriding.

class Animal:
    def speak(self):
        return "Animal makes a sound."

class Dog(Animal):
    def speak(self):
        return "Dog barks."

class Cat(Animal):
    def speak(self):
        return "Cat meows."

dog = Dog()
cat = Cat()

print(dog.speak()) 
print(cat.speak())