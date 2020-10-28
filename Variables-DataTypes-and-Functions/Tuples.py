'''
Make a tuple and print the last item using indexing.
'''
tuple = ("Hello", 3, 4.6)
print(tuple)
print("Data Type of an item in Tuple:",type(tuple[2]))
print("Print the last element of the tuple:",tuple[-1])
print()

person_1 = ('Nishant', 25, 'Computer')
person_2 = ('Kunal', 23, 'Camera')

people = [person_1, person_2]

for name, age, tool in people:
    print(name)
    print(age)
    print(tool)
    print()