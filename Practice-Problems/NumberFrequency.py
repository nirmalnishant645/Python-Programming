l = input("Enter the numbers in the list: ").split()
l = list(map(int, l))
done = []

for i in l:
    if (i in done):
        continue
    else:
        print(("The frequency of %d is %d") % (i, l.count(i)))
        done.append(i)
