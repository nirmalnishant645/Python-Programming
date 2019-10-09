import re

text = input("Enter a string: ")

if re.search('^[a-zA-Z0-9_]*$',  text):
        print("Accepted Input: ",text)
else:
        print("Invalid Input!")
