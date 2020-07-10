'''
A singly linked list is a collection of nodes in a linear sequence.
Each node stores a reference to an object that is an element of the sequence,
as well as a reference to the next node.
List also maintains a member called 'head' that identifies the first node of the list.
Next reference of a node can be thought of as a link or a pointer to another node.

*It does not have a predetermined fixed size.
'''

class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class Linked_list:
	def __init__(self):
		self.head = Node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self, data):
		new_node = Node(data)
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total 

	# Prints out the linked list. 
	def display(self):
		cur_node = self.head
		while cur_node.next != None:
			cur_node = cur_node.next
			print(cur_node.data, end = " ")
		print('')

	# Returns the value of the node at 'index'. 
	def get(self, index):
		if index >= self.length() or index < 0: 
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_idx == index:
			    return cur_node.data
			cur_idx += 1

	# Deletes the node at index 'index'.
	def erase(self, index):
		if index >= self.length() or index < 0:
			print("ERROR: 'Erase' Index out of range!")
		cur_idx = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_idx == index:
				last_node.next = cur_node.next
				return None
			cur_idx += 1

	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self, index):
		return self.get(index)

	'''
	Inserts a new node at index 'index' containing data 'data'.
	Indices begin at 0. If the provided index is greater than or 
	equal to the length of the linked list the 'data' will be appended.
	If index is less than zero, warning will be printed to the user.
	'''
	def insert(self, index, data):
	    if index >= self.length() or index < 0:
	        print("ERROR: 'Insert' Index out of range!")
	    cur_node = self.head
	    prior_node = self.head
	    cur_idx = 0
	    while True:
		    cur_node = cur_node.next
		    if cur_idx == index: 
			    new_node = Node(data)
			    prior_node.next = new_node
			    new_node.next = cur_node
			    return None
		    prior_node = cur_node
		    cur_idx += 1
	
	'''
    Sets the data at index 'index' equal to 'data'.
    Indices begin at 0. If the 'index' is greater than or equal 
    to the length of the linked list a warning will be printed 
    to the user.
    '''	
	
	def set(self, index, data):
	    if index >= self.length() or index < 0:
	        print("ERROR: 'Set' Index out of range!")
	    cur_node = self.head
	    cur_idx = 0
	    while True:
	        cur_node = cur_node.next
	        if cur_idx == index:
	            cur_node.data = data
	            return None
	        cur_idx += 1
