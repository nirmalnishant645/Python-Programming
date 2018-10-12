'''
Use for loop to take the items of two lists at once and print them together.
'''
names = ['nishant', 'nirmal', 'anant']
email_domains = ['gmail', 'hotmail', 'yahoo']

for i,j in zip(names,email_domains):
    print(i,'@',j,'.com')
