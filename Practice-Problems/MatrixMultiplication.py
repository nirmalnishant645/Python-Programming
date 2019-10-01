Ar, Ac = input("Enter the Rows and Columns of First matrix seperated by space: ").split()
Br, Bc = input("Enter the Rows and Columns of Second matrix seperated by space: ").split()


A = []
B = []
Result = []

for i in range(int(Ar)):
	Row=[]
	for j in range(int(Ac)):
		R=int(input(("Enter the element A(%d,%d)")%(i,j)))
		Row.append(R)
	A.append(Row)

for i in range(int(Br)):
	Row=[]
	for j in range(int(Bc)):
		R=int(input(("Enter the element B(%d,%d)")%(i,j)))
		Row.append(R)
	B.append(Row)

for i in range(int(Ar)):
	Row=[]
	for j in range(int(Bc)):
		Row.append(0)
	Result.append(Row)

print(A,"\n",B,"\n",Result)

for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			Result[i][j]+=(A[i][k])*(B[k][j])
for i in Result:
	print(i)
