'''
Define a function that gets Celsius degrees as input and returns Fahrenheit, or a message if the Celsius inputvalue is less than -273.15
Implement a for loop that iterates through the following temperatures list temperatures=[10,-20,-289,100]and calls the above c_to_f function in each iteration.
'''
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for t in temperatures:
    print(c_to_f(t))
