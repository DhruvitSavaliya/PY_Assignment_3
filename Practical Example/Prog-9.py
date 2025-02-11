#Write a Python program to handle file exceptions and use the finally block for closing 
#the file.

file = None
try:
    file_name = input("Enter the name of the file to open: ")
    file = open(file_name, 'r')
    content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print("Error: The specified file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print("An unexpected error occurred: ",e)

finally:
    if file:
        file.close()
        print("File has been closed.")