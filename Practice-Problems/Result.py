def result(x,y,z):
	if (x+y+z>=210):
		return "1st"
	elif (180<=x+y+z<210):
		return "2nd"
	elif (150<=x+y+z<210):
		return "3rd"
	elif (x+y+y<150):
		return "4th"

x = int(input("Enter the marks of Subject 1: "))
y = int(input("Enter the marks of Subject 2: "))
z = int(input("Enter the marks of Subject 3: "))

print(result(x,y,z),"Division")
