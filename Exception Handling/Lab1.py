#Write a Python program to handle exceptions in a simple 
# calculator (division by zero, invalid input).

try:
    n1 = int(input("Enter First number  : "))
    n2 = int(input("Enter Second number : "))
    ans =n1/n2
    print("Answer : ",ans)
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error : ",e)