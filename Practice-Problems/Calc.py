'''
Program to make a simple calculator
'''
def add(a,b):
	return a+b
def mult(a,b):
	return a*b
def sub(a,b):
	return a-b
def div(a,b):
	return a/b
	

a = int(input("Enter the First Operand: "))
b = int(input("Enter the Second Operand: "))
c = input("Select the Operator '+', '-', '*', '/': ")

if (c == '+'):
	print(add(a,b))
elif (c == '-'):
	print(sub(a,b))
elif (c == '*'):
	print(mult(a,b))
elif (c == '/'):
	print(div(a,b))
else:
	print("Invalid Operator!")


