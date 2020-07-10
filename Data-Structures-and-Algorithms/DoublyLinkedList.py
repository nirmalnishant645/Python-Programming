'''
Doubly Linked List is a variation of Linked list in which navigation is possible in both ways,
either forward and backward easily as compared to Single Linked List.
Each node stores a reference to an object that is an element of the sequence, and  a reference to the next node,
just like in the case of singly linked list, but in this case, it will also store a reference to the previous node.
This allows a greater variety of O(1)-time update operations.
List also maintains two members called 'head' and 'tail' that identifies the first and the last node of the list respectively.
Next or Prev reference of a node can be thought of as a link or a pointer to another node.

* It does not have predetermined fixed size.

PROS:
    Can be traversed in both forward and backward direction.
    The delete operation in DLL is more efficient if the pointer to the node to be deleted is given.
    We can quickly insert a new node before a given node.
CONS:
    Every node of DLL Requires extra space for a previous pointer.
    All operations require an additional pointer previous to be maintained.
'''

# Node() creates a new node that contains a value and a reference to the next and the previous node.
# It needs value of the node as parameter or it will be assigned as None.
class Node(object):

    def __init__(self, value = None):

        self.value = value
        self.next_node = None
        self.prev_node = None

# DoublyLinkedList() creates a new doubly linked list with a head and a tail node whose values are None.
# It needs no parameter and returns a linked list with an empty head node and an empty tail node.
class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    # Adds a new node at the beginning of the linked list.
    def prepend(self, value):   # It needs only one parameter the value of the new node and returns nothing.
        new_node = Node(value)
        if self.head:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node    # Link List is modified.
        else:
            self.head = self.tail = new_node

    # Adds a new node at the end of the linked list.
    def append(self, value):    # It needs only one parameter the value of the new node and returns nothing.
        new_node = Node(value)
        if self.tail:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node    # Link List is modified
        else:
            self.tail = self.head = new_node

    # Returns the number of nodes in the linked list.
    def length(self):   # It needs no parameter and returns the length of the linked list.
        total_nodes = 0
        cur_node = self.head
        while cur_node:
            total_nodes += 1
            cur_node = cur_node.next_node
        return total_nodes

	# Displays all the nodes of the linked list in order.
    def display(self):
        cur_node = self.head
        print('None', end = "")
        while cur_node:
            print(" <- ", end = "")
            print(cur_node.value, end = " -> ")	# Only prints each node of the linked list.
            cur_node = cur_node.next_node
        print('None')

    # Inserting a new node in the linked list after a node using the reference to that node.
    def insert_after(self, ref_node, value):    # It needs reference to the node as parameters and inserts a new node after that node.
        if not ref_node:
            raise ValueError('Node does not exist!')    # If the node is not in the linked list then error is raised.
        new_node = Node(value)
        new_node.prev_node = ref_node
        if not ref_node.next_node:
            self.tail = new_node
        else:
            new_node.next_node = ref_node.next_node
            new_node.next_node.prev_node = new_node
        ref_node.next_node = new_node   # Linked List is modified

    # Inserting a new node in the linked list before a node using the reference to that node.
    def insert_before(self, ref_node, value):   # It needs reference to the node as parameters and inserts a new node after that node.
        if not ref_node:
            raise ValueError('Node does not exist!')
        new_node = Node(value)
        new_node.next_node = ref_node
        if not ref_node.prev_node:
            self.head = new_node
        else:
            new_node.prev_node = ref_node.prev_node # Linked List is modified.

    # Getting the value of a node from linked list using index.
    def __getitem__(self, index):   # It needs index as a parameter and returns the value of the node at that index.
        if index >= self.length() or index < 0:
            raise IndexError("Index out of range!") # If the index is not in range of the linked list then error is raised.
        cur_index = 0
        cur_node = self.head
        while cur_node:
            if cur_index == index:
                return cur_node # Linked List is not modified.
            cur_index += 1
            cur_node = cur_node.next_node

    # Deleting a node from the linked list.
    def remove(self, node): # It needs reference to the node  to be deleted as a parameter and deletes that node but returns nothing.
        if not node:
            raise ValueError('Node does not exsit!') # If the node is not in the linked list then error is raised.
        if not node.prev_node:
            self.head = node.next_node
        else:
            node.prev_node.next_node = node.next_node
        if not node.next_node:
            self.tail = node.prev_node  # Link list is modified.
        else:
            node.next_node.prev_node = node.prev_node

list = DoublyLinkedList()

list.append(1)

list.prepend(2)

list.append(1)

list.prepend(7)

print(list.length())

list.display()

list.insert_after(list[0], 3)

list.display()

list.insert_before(list[2], 7) #

list.display()

print(list[2].value)

list.remove(list[3])

print(list.length())

list.display()