'''
Define a function to calculate age after 50 years and take input as age from the user and print the new age
'''
def age_fifty(age):
    new_age = float(age) + 50
    return new_age

age = input("Enter your age: ")
print(age_fifty(age))
