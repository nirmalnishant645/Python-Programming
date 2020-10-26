digits = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(digits)):
    print(digits[0:i])

window_size = 3

for i in range(len(digits)-(window_size-1)):
    print(digits[i:i+window_size])