'''
Python program to count the number of even odd numbers from a series of numbers 5 to 100
'''
even_count, odd_count = 0 , 0

for num in range(5,101):
	if (num%2 == 0):
		even_count+=1
	else:
		odd_count+=1

print("Even numbers are: ",even_count)
print("Odd numbers are: ",odd_count)
