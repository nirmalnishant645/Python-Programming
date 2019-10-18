a = input("Enter the name of the file with extension: ")

print("Reverse in 1st Way:\n")

for line in open(a, 'r'):
	print(' '.join(line.split()[::-1]))


print("Reverse in 2nd Way:\n")

for line in reversed(list(open(a))):
    print(line.rstrip())
