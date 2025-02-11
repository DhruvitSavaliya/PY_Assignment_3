#Write a Python program to open a file in write mode, write some text, and then close it.

import random

text = open("text1.txt","w")

for i in range(10):
    num=random.randint(1,100)
    text.write(str(num)+",")

text.close()
