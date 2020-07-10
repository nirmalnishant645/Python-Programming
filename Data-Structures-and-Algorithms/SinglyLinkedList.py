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

class Node(object):

	def __init__(self, value = None):
	 
	 self.value = value
	 self.next_node = None

class LinkedList(object):

	def __init__(self):

		self.head = Node()

	def append(self, value):
		new_node = Node(value)
		cur_node = self.head
		while cur_node.next_node:
			cur_node = cur_node.next_node
		cur_node.next_node = new_node

	def length(self):
		cur_node = self.head
		total_nodes = 0
		while cur_node.next_node:
			total_nodes += 1
			cur_node = cur_node.next_node
		return total_nodes

	def display(self):
		cur_node = self.head
		while cur_node.next_node:
			cur_node = cur_node.next_node
			print(cur_node.value, end = " ")
		print('')

	def __getitem__(self, index):
		if index >= self.length() or index < 0:
			raise IndexError("Index out of range!")
		cur_index = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next_node
			if cur_index == index:
				return cur_node.value
			cur_index += 1

	def __delitem__(self, index):
		if index >= self.length() or index < 0:
			raise IndexError("Index out of range!")
		cur_index = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next_node
			if cur_index == index:
				last_node.next_node = cur_node.next_node
				return None
			cur_index += 1

	def  __setitem__(self, index, value):
		if index > self.length() or index < 0:
			raise IndexError("Index out of range!")
		cur_node = self.head
		cur_index = 0
		while True:
			cur_node = cur_node.next_node
			if cur_index == index:
				cur_node.value = value
				return None
			cur_index += 1

	def insert(self, index, value):
		if index > self.length() or index < 0:
			raise IndexError("Index out of range!")
		if index == self.length:
			self.append(value)
		cur_node = self.head
		prev_node = self.head
		cur_index = 0
		while True:
			cur_node = cur_node.next_node
			if cur_index == index:
				new_node = Node(value)
				prev_node.next_node = new_node
				new_node.next_node = cur_node
				return None
			prev_node = prev_node.next_node
			cur_index += 1