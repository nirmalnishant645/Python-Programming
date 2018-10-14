'''
Open a file and print it's lines in the form of a list after stripping out '\n'.
After that, also close the file using file.close()
'''
file = open("example.txt",'r')
content = file.readlines()
content = [i.rstrip("\n") for i in content]
print(content)
file.close()
