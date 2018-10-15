'''
Program that reads the content of the file and prints out the length of each line.

Expected output:

4
5
6
8
10
11
'''
file = open("fruits.txt", "r")
content = file.readlines()
file.close()
for i in content:
     print(len(i.strip()))
