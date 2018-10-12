'''
Use while loop to compare password entered by the user and print if it is correct or not.
'''
password = ''
while password != 'python123':
    password = input("Enter Password: ")
    if password == 'python123':
        print("You are logged in.")
    else:
        print("Sorry, wrong password!")
