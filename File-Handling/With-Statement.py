'''
Open a file using with statement and add a new line
'''
with open("example3.txt","a+") as file:
    file.seek(0)
    content = file.read()
    file.write("Line 6")
    file.close()
