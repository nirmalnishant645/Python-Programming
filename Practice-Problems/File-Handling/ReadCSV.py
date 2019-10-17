import csv

a = input("Enter the file name with .csv extension to read from: ")

with open(a, 'r') as i:
	read = csv.reader(i)
	csvDict = {rows[0]:rows[1] for rows in read}

print(csvDict)
