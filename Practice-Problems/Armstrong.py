'''
Program to input a number and check if the number is Armstrong number or not
'''
num = int(input("Enter a number: "))
sum = 0
temp = num

while(temp>0):
	digit=temp%10	
	sum+=digit**3
	temp//=10

if num == sum:
	print(num,"is an Armstrong Number")
else:
	print(num,"is not an Armstrong Number")
