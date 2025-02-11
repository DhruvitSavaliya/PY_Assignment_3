#Write a Python program to search for a word in a string using re.search().

import re

text = "Hello, welcome to the world of Python programming."

word = "Python"

match = re.search(word,text)

if match:
    print("Word  found .")
else:
    print("Word  not found .")