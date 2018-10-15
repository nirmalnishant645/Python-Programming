'''
Write some code that creates a text file and writes the items of list to that text file.
'''
file = open("example1.txt",'w')
l=["Line number 1","Line number 2","Line number 3"]
for item in l:
    file.write(item+"\n")
file.close()
