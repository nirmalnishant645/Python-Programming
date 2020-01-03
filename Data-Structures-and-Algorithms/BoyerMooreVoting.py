#Moore's Voting Algorithm to find the majority element (element that appears more than n/2 times)

def boyerMoore(arr):
	count = ans = 0
	for n in nums:
		if count == 0:
			ans = n
		count += 1 if ans == n else -1
	return ans

