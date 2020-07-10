'''
Write a function to reverse a Linked List in place.
The function will take in the head of the list as input and return the new head of the list.
You have been given the Linked List Node class code.
'''

#   Time Complexity - O(n)
#   Space Complexity - O(1)

class Node(object):

    def __init__(self, value):

        self.value = value
        self.next_node = None

def reverse(head):
    
    cur_node = head
    prev_node = None
    next_node = None

    while cur_node:

        next_node = cur_node.next_node
        cur_node.next_node = prev_node
        prev_node = cur_node
        cur_node = next_node

    return prev_node