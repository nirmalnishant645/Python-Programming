'''
Define a function to calculate the age of the user after 50 years and first check if it is less than 125 or not, if yes then print the new age otherwise don't.
'''
def age_fifty(age):
    new_age = age + 50
    return new_age

age = float(input("Enter your age: "))

if age < 125:
    print(age_fifty(age))
else:
    print("Possibly an absurd age.")
