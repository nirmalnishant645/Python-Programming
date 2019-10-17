a = input("Enter the name of the file with extension: ")

lines=words=chars=0

with open(a, 'r') as f:
	for line in f:
		word = line.split(' ')
		lines+=1
		words+=len(word)
		chars+=len(line)

print("Number of Lines = %d\nNumber of Words = %d\nNumber of Characters = %d" % (lines, words, chars))
