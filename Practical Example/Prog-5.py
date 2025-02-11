# Write a Python program to read a file and print the data on the console.

data = open("prog5.txt","r")
line = data.readline()

while(line!=""):
    print(line)
    line = data.readline()

data.close()
