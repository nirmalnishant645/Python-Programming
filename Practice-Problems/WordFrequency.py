a = input("Enter a string: ").split()
a = list(map(str, a))
d = {}
for i in a:
    d[i] = d.get(i,0) + 1

for m,n in d.items():
    print(("Frequency of %s is %d") % (m,n))
