'''
Write a function that takes a head node and an integer value n,
and then returns the nth to last node in the linked list.

For example, given:

class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None

Example Input and Output:

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

target_node = nth_to_last_node(2, a) = d
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None

def nth_to_last_node(n, head):

    left = right = head

    for i in range(n - 1):
        
        if not right.next_node:
            raise LookupError('n is larger than the linked list!')

        right = right.next_node

    while right.next_node:

        left = left.next_node
        right = right.next_node

    return left