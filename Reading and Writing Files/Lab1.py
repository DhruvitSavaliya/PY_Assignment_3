#Write a Python program to read the contents of a file and print them on the console.

data = open("lab1.txt","r")
line = data.readline()

while(line!=""):
    print(line)
    line = data.readline()

data.close()
