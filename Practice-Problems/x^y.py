def power(x,y):
	result = 1

	while(y!=0):
		result*=x
		y-=1		

	return result

x = int(input("Enter the value of x(Base): "))
y = int(input("Enter the value of y(Power): "))

print("x^y = ",power(x,y))
