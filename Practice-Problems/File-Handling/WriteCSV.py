import csv

a = input("Enter the file name with .csv extension to write in: ")

l = [[1, 2, 3, 5, 7], 3, 1, 3, 4, [5, 6, 4, 6], 31, 43, 21, [21, 53, 31], [21, 21, 42, 452, 42, 5634], [53, 21, 42, 64, 75, 64, 64] , 86, 654, 643, 98]

with open(a, 'w') as i:
	write = csv.writer(i)
	write.writerow(j for j in l)
