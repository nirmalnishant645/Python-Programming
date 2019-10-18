# Program to input total marks scored by a student and number of sections in exam
# Raise exception if the number of sections is <1 or the marks entered are –ve or the marks are more than 100.

n = int(input("Enter the number of records you want to input: "))

name = [0]*n
marks = [0]*n
section = [0]*n

for i in range(n):
    name[i], marks[i], section[i] = input("Enter Name: "), int(input("Enter Marks: ")), int(input("Enter Section: ")) 
    if (marks[i]<0 or marks[i]>100):
        try:
            raise ValueError('Marks is out of range!')
        except ValueError:
            print('An exception flew by!')
            raise
    elif (section[i]<1):
        try:
            raise ValueError('Section is out of range!')
        except ValueError:
            print('An exception flew by!')
            raise

print(name, marks, section)
