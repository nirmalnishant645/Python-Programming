'''
Use for loop to print all the items of a list at once
'''
emails = ['nishant@gmail.com', 'nirmalhotmail.com', 'nn@gmail.com']
'''
To Print all emails
'''
print("All emails in the list")
for  email in emails:
    print(email)
'''
To Print only the Gmail emails
'''
print("Only Gmail: ")
for item in emails:
    if 'gmail' in item:
        print(item)
