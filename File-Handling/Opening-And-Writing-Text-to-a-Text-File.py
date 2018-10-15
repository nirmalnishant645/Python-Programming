file = open("example1.txt",'w')
l=["Line number 1","Line number 2","Line number 3"]
for item in l:
    file.write(item+"\n")
file.close()
