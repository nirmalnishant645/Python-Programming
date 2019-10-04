import re

email = input("Enter the email address: ")

if(re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email)):
    print("Valid Email")
else:
    print("Invalid Email")
