'''
Create a function that converts Celsius degrees to Fahrenheit.
The formula to convert Celsius to Fahrenheit is F= C 9/5 + 32.
'''
def cel_to_fahr(c):
    f = float(c) * 9/5 + 32
    return f

c = input("Enter Temperature in Celcius: ")
print(cel_to_fahr(c))
