import re
a = input("Enter a string: ")
if re.search('a.*?b$',  a):
    print("Found a match!")
else:
    print("Not matched!")
