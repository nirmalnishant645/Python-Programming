a = input("Enter a string: ").split()
a = list(map(str, a))
d = {}
for i in a:
    d[i] = len(i)

print("Dictionary:\n",d)
