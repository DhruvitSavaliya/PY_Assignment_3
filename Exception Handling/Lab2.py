#Write a Python program to demonstrate handling multiple exceptions. 

try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        num1 = int(num1)
        num2 = int(num2)

        result = num1 / num2
        print("Result of division:",result)

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print("An unexpected error occurred:",e)