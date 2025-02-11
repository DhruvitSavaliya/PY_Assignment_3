#Write a Python program to create a class and access the properties 
#of the class using an object.

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Student Name : ",self.name)
        print("Student Age : ",self.age)

s1 = student("Dhruvit",20)
s1.display()
print()
s2 = student("Vivek",20)
s2.display()
