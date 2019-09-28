'''
Program to display all the prime numbers within an interval
'''
l = int(input("Enter the lower limit of the interval: "))
u = int(input("Enter the upper limit of the interval: "))

print("Prime Numbers between", l, "and", u, "are: ")

for num in range(l,u+1):
	if (num>1):
		for i in range(2,num):
			if(num%i==0):
				break
		else:
			print(num)
