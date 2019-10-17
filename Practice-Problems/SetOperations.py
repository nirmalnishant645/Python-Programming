A = set(input("Enter the elements of the first Set: ").split())
B = set(input("Enter the elements of the second Set: ").split())

print("Set A =",A,"\nSet B =",B)

print("\nUnion of A and B is",A | B)

print("\nIntersection of A and B is",A & B)

print("\nDifference of A and B is",A - B)

print("\nSymmetric difference of A and B is",A ^ B)
