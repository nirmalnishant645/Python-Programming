'''
Create a function that takes any string as argument and returns the length of that string.
The lowest possible temperature that physical matter can reach is -273.15 C.
With that in mind, please improve the function by making it print out a message in case a number lower than -273.15 is passed as input when calling the function.
'''
def cel_to_fahr(c):
    if c < -273.15:
        return "Absurd Temperature Value"
    else:
        f = float(c) * 9/5 + 32
        return f

c = float(input("Enter Temperature in Celcius: "))
print(cel_to_fahr(c))
