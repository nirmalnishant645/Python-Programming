
def printn(num):
	if (num == 0):
		return
	print("*", end = "")

	printn(num - 1)

def pattern(n, i):
	if (n == 0):
		return
	printn(i)
	print("\n", end = "")

	pattern(n - 1, i + 1)

if __name__ == '__main__':
	n = 4
	pattern(n, 1)
