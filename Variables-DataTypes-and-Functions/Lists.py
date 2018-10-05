'''
Make a list, check its indexing, check data types of the items of the list, split the items of the list, add a new item in the list and remove items from the list.
'''
list = ["H", 2, "Hello"]
print("Index 0:",list[0])
print("Index 2",list[2])
print("Data Type of first item in the list:",type(list[0]))
print("Data Type of second item in the list:",type(list[1]))
print("Accesing more than one items of the list:",list[:2])
'''
Adding New item to the list
'''
list.append(3)
print("After Addition:",list)
'''
Remove an item from the list
'''
list.remove(2)
print("After Removal:",list)
