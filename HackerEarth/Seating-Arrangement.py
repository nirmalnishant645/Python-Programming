'''
Akash and Vishal are quite fond of travelling.
They mostly travel by railways.
They were travelling in a train one day and they got interested in the seating arrangement of their compartment.
The compartment looked something like

WS  MS  AS      AS  MS  WS
1	2	3	   	4	5	6
12	11	10	   	9	8	7
--------------------------
13	14	15	   	16	17	18
24	23	22	   	21	20	19
--------------------------
25	26	27	   	28	29	30
36	35	34	   	33	32	31
--------------------------
37	38	39	   	40	41	42
48	47	46	   	45	44	43
--------------------------
49	50	51	   	52	53	54
60	59	58	   	57	56	55
--------------------------
61	62	63	   	64	65	66
72	71	70	   	69	68	67
--------------------------
73	74	75	   	76	77	78
84	83	82	   	81	80	79
--------------------------
85	86	87	   	88	89	90
96	95	94	   	93	92	91
--------------------------
97	98	99	   	100	101	102
108	107	106	   	105	104	103

So they got interested to know the seat number facing them and the seat type facing them.
The seats are denoted as follows :

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number,
find out the seat number facing you and the seat type,
i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases.
Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type,
separated by a single space in a new line.

CONSTRAINTS
1<=T<=105
1<=N<=108
'''