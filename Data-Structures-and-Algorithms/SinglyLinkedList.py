'''
A singly linked list is a collection of nodes in a linear sequence.
Each node stores a reference to an object that is an element of the sequence,
as well as a reference to the next node.
List also maintains a member called 'head' that identifies the first node of the list.
Next reference of a node can be thought of as a link or a pointer to another node.

*It does not have a predetermined fixed size.

PROS:
	Linked lists have a constant insertions and deletions in any position,
	in comparison, arrays require O(n) time to do the same thing.
	Linked Lists can continue to expand without having to specify the size ahead of time.

CONS:
	To access an element in a linked list, you need to take O(k) time
	to go from the head of the list to the kth element.
	In contrast, arrays have a constant time operations to access elements in an array.
'''

# Node() creates a new node that contains a value and a reference to the next node.
# It needs value of the node as parameter or it will be assigned as None.
class Node(object):

	def __init__(self, value = None):
	 
	 self.value = value
	 self.next_node = None

# LinkedList() creates a new linked list with a head node whose value is None.
# It needs no parameter and returns a linked list with only a head node.
class LinkedList(object):

	def __init__(self):

		self.head = Node()

	# Adds a new node at the end of the linked list.
	def append(self, value):	# It needs only parameter the value of the new node and returns nothing.
		new_node = Node(value)
		cur_node = self.head
		while cur_node.next_node:
			cur_node = cur_node.next_node
		cur_node.next_node = new_node	# Linked List is modified

	# Returns the number of nodes in the linked list.
	def length(self):	# It needs no parameter and returns the length of the linked list.
		cur_node = self.head
		total_nodes = 0
		while cur_node.next_node:
			total_nodes += 1
			cur_node = cur_node.next_node
		return total_nodes

	# Displays all the nodes of the linked list in order
	def display(self):	# It needs no parameter and returns nothing.
		cur_node = self.head
		while cur_node.next_node:
			cur_node = cur_node.next_node
			print(cur_node.value, end = " -> ")	# Only prints each node of the linked list.
		print('None')

	# Getting the value of a node from linked list using index.
	def __getitem__(self, index):	# It needs index as a parameter and returns the value of the node at that index.
		if index >= self.length() or index < 0:
			raise IndexError("Index out of range!")	# If the index is not in range of the linked list then error is raised.
		cur_index = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next_node
			if cur_index == index:
				return cur_node.value	# Linked List is not modified.
			cur_index += 1

	# Deleting a node from the linked list using index.
	def __delitem__(self, index):	# It needs index as a parameter and deletes the node at that index but returns nothing.
		if index >= self.length() or index < 0:
			raise IndexError("Index out of range!")	# If the index is not in range of the linked list then error is raised.
		cur_index = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next_node
			if cur_index == index:
				last_node.next_node = cur_node.next_node	# Linked list is modified.
				return None
			cur_index += 1

	# Setting the value of an already existing node of the linked list using index.
	def  __setitem__(self, index, value):	# It needs index and value as parameters and sets the value of node at that index.
		if index >= self.length() or index < 0:
			raise IndexError("Index out of range!")	# If the index is not in range of the linked list then error is raised.
		cur_node = self.head
		cur_index = 0
		while True:
			cur_node = cur_node.next_node
			if cur_index == index:
				cur_node.value = value	# Linked List is modified.
				return None
			cur_index += 1

	# Inserting a new node in the linked list using index (Not modiying the node that already exists at that index).
	def insert(self, index, value):	# It needs index and value as parameters and inserts a new node at that index and pushes the next nodes to next indices.
		if index > self.length() or index < 0:
			raise IndexError("Index out of range!")	# If the index is not in range of the linked list then error is raised.
		if index == self.length:	# It will append a new node if the index passed is equal to the length of the linked list.
			self.append(value)
		cur_node = self.head
		prev_node = self.head
		cur_index = 0
		while True:
			cur_node = cur_node.next_node
			if cur_index == index:
				new_node = Node(value)
				prev_node.next_node = new_node
				new_node.next_node = cur_node	# Linked list is modified.
				return None
			prev_node = prev_node.next_node
			cur_index += 1