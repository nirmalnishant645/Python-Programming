string = input("Enter a string: ")
substring = input("Enter the substring to find in the string: ")

if (string.find(substring)>=0):
    print("Position:",string.find(substring))
else:
    print("Not found!")
