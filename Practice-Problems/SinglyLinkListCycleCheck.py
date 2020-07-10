'''
Given a singly linked list, write a function which takes in the first node in a singly linked list
and returns a boolen indicating if the linked list contains a "cycle".
A cycle is when a node's next point actually points back to a previous node in the list.
This is also known as a circularly linked list.
You have been given the Linked List Node class code.
'''

# Floyd's Tortoise and Hare Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node(object):

    def __init__(self, value):
        
        self.value = value
        self.next_node = None

def cycle_check(node):
    
    hare = tortoise = node

    while hare and hare.next_node:

        tortoise = tortoise.next_node
        hare = hare.next_node.next_node

        if tortoise == hare:
            return True

    return False