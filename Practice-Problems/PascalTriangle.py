'''
Write a function to print first 'n' rows of Pascal's Triangle
'''
def PascalTriangle(n):
	row = [1]
	a = [0]
	for i in range(max(n,0)):
		print(row)
		row = [x+y for x,y in zip(row+a, a+row)]
	return n>=1
n = int(input("Enter the number of rows: "))
PascalTriangle(n)
