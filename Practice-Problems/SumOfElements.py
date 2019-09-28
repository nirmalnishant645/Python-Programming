def sum(n):
	while(n>=10):
		summ=0
		while(n>0):
			summ=summ+n%10
			n=n//10
		n=summ
	else:
		print(n)
n = int(input("Enter the number: "))
sum(n)
