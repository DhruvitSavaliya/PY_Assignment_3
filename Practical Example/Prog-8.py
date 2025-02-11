#Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
        file_name = input("Enter the name of the file to open: ")
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print("Result of division: ",result)

except FileNotFoundError:
    print("Error: The specified file was not found.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values where required.")
except Exception as e:
    print("An unexpected error occurred: ",e)