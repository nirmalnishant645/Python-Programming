'''
Program that reads the content of the file and generates the following output in the command line:

pear
apple
orange
mandarin
watermelon
pomegranate
'''
file = open("fruits.txt", "r")
content = file.read()
file.close()
print(content)
