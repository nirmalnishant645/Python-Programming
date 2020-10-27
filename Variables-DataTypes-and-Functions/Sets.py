list_of_numbers = [1, 4, 3, 5, 6, 7, 3, 4, 5, 8, 2, 7, 3, 8, 5, 6, 9]

no_duplicate = set(list_of_numbers)

print(no_duplicate)

library_1 = {'Harry Potter', 'Lord of the Rings', 'Hunger Games'}
library_2 = ('Harry Potter', 'Romeo & Juliet')

all_books = library_1.union(library_2)

print(all_books)

common_books = library_1.intersection(library_2)

print(common_books)