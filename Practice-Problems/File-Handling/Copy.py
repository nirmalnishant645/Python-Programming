a = input("Enter the file name to be copied from: ")
b = input("Enter the file name in which to be copied: ")

A = open(a, 'r')
B = open(b, 'a')

for i in A.readlines():
	B.write(i)
A.close()
B.close()
