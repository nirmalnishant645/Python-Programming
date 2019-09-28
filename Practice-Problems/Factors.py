'''
Program to find all the factors of x
'''
x = int(input("Enter the number: "))

print("The factors of", x,"are: ")

for i in range(1,x+1):
	if(x%i==0):
		print(i)
