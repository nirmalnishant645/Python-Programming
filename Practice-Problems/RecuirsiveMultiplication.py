def RMult(n, m):
	if m == 0:
		return 0
	elif m < 0:
		return - (n - RMult(n, m+1))
	else:
		return n + RMult(n, m-1)

n = int(input("Enter the first integer: "))
m = int(input("Enter the second integer: "))

print("Product of {0} and {1} is".format(n,m), RMult(n, m))
