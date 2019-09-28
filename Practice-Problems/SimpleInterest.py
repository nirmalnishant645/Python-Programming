'''
Program to compute a Simple Calculator
'''
p = int(input("Enter the Principal Amount: "))
t = int(input("Enter the Time: "))
r = float(input("Enter the Rate of Interest: "))
si = 0.0

si = p * t * r / 100

print(si)
