from itertools import permutations

A = input("Enter three digits: ")
B = permutations(A,3)

for i in B :
    print(''.join(i))
