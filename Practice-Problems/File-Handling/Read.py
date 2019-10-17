a = input("Enter the name of the file with extension: ")
toRead = open(a, 'r')
line = toRead.readline()
while(line!=""):
	print(line)
	line = toRead.readline()
toRead.close()
