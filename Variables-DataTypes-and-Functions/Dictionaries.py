'''
Make a dictionary and access its items
'''
a = {"First_Name":"Nishant", "Last_Name":"Nirmal", "Cities":("Patna", "Kolkata", "New Delhi")}
'''Accesing item using Key'''
print(a["First_Name"])
print(a["Cities"])
'''Accesing a nested item (Item inside a List or Tuple)'''
print(a["Cities"][2])


contacts = {
    'Nishant' : {'Phone' : '8563782018', 'Email' : 'nirmalnishant645@gmail.com'},
    'Sachin' : {'Phone' : '6472839201', 'Email' : 'sachin_t@yahoo.co.in'},
    'Roger' : {'Phone' : '7485930492', 'Email' : 'rf_007@rediff.co.in'}
}

print(contacts['Nishant']['Phone'])
print(contacts['Sachin'])
print(contacts['Roger']['Email'])

print(contacts.items())
print(contacts.keys())
print(contacts.values())