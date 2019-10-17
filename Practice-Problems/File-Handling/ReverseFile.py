a = input("Enter the name of the file with extension: ")

for line in reversed(list(open(a))):
    print(line.rstrip())
