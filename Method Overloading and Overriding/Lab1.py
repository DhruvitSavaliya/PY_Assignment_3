#Write Python programs to demonstrate method overloading and method overriding.

#method overloading...

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(5))          
print(calc.add(5, 10))      
print(calc.add(5, 10, 15)) 

#method overriding....

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
