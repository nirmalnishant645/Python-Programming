'''
Problem:
Bob's crush's name starts with a vowel. That's the reason Bob loves vowels too much.
He calls a string "lovely string" if it contains either all the lowercase vowels or all the uppercase vowels or both,
else he calls that string "ugly string". 

For more clarification, see the sample testcase explanation.

Input:
First line contains T, the number of test cases.
Next T lines contain a single string S.

Output:
For each test case, print "lovely string" or "ugly string"  (without quotes)  according to the definition of Bob.

Constraints:
string contains only lowercase and uppercase Latin letters. 
1<=T<=100
1<=len(S)<=100000

Sample Input:
3
omahgoTuRuLob
OmAhgotUrulobEI
aeKORONAoiBATCHu

Sample Output:
ugly string
lovely string
lovely string

Explanation:
In first string, neither all five lowercase vowels are present nor all five uppercase vowels.
In second string, all five uppercase vowels are present.
In third string ,  all five lowercase vowels are present.
'''
i = int(input())

while i:
    upper_case = ['A', 'E', 'I', 'O', 'U']
    lower_case = ['a', 'e', 'i', 'o', 'u']
    test_string = input()
    for j in test_string:
        if j in upper_case:
            upper_case.remove(j)
        elif j in lower_case:
            lower_case.remove(j)
    if not upper_case or not lower_case:
        print('lovely string')
    else:
        print('ugly string')
    i -= 1
