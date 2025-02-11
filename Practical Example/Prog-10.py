#Write a Python program to print custom exceptions. 

class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

file = None
try:
    file_name = input("Enter the name of the file to open: ")
    if not file_name.endswith('.txt'):
        raise CustomException("Only .txt files are allowed.")

    file = open(file_name, 'r')
    content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print("Error: The specified file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except CustomException as ce:
    print(f"Custom Error: {ce}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if file:
        file.close()
        print("File has been closed.")
