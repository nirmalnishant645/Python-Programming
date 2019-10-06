A = input("Enter the elements of the first Set: ").split()
A = set(map(int, A))
B = input("Enter the elements of the second Set: ").split()
B = set(map(int, B))

print("Set A =",A,"\nSet B =",B)

print("\nUnion of A and B is",A | B)

print("\nIntersection of A and B is",A & B)

print("\nDifference of A and B is",A - B)

print("\nSymmetric difference of A and B is",A ^ B)
