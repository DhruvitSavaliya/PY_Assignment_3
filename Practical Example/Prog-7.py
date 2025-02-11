# Write a Python program to handle exceptions in a calculator.

try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        ch = input("Enter an operation (+, -, *, /): ").strip()

        if ch == '+':
            result = num1 + num2
        elif ch == '-':
            result = num1 - num2
        elif ch == '*':
            result = num1 * num2
        elif ch == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation. Please choose one of +, -, *, /.")

        print("The result is: ",result)

except ValueError as e:
        print("Error: ",e)
except ZeroDivisionError as e:
        print("Error: ",e)
except Exception as e:
        print("An unexpected error occurred: ",e)


