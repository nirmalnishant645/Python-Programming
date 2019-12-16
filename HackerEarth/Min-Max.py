'''
Given A Series Of N Positive Integers a1,a2,a3........an. , Find The Minimum And Maximum Values That Can Be Calculated By Summing Exactly N-1 Of The N Integers. Then Print The Respective Minimum And Maximum Values As A Single Line Of Two Space-Separated Long Integers.

Input Format
First Line Take Input Value Of N
Second Line Take Input N Space Separated Integer Value

Output Format
Two Space Separated Value ( One Maximum Sum And One Minimum Sum )

Constraints
0 < N < 100001
0 <= ai < 1013

SAMPLE INPUT
5
1 2 3 4 5

SAMPLE OUTPUT
10 14
'''
n = int(input())
series = list(map(int, input().split()))
