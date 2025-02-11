#Write a Python program to demonstrate the use of local and 
#global variables in a class.

global_variable = "Hello,"

class demo:
    def __init__(self,local_variable):
        self.local_variable=local_variable

    def display(self):
        print("global_variable String : ",global_variable)
        print()
        print("local_variable String : ",self.local_variable)

d = demo("How are You")
d.display()
