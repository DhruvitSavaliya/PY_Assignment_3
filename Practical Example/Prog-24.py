#Write a Python program to match a word in a string using re.match(). 

import re

text = "Python is a powerful language."

word = "Python"

match = re.match(word,text)

if match:
    print("Word  found .")
else:
    print("Word  not found .")