'''
FIRST IN FIRST OUT (FIFO)
ENQUEUE - Adding a new item to the rear of the queue.
DEQUEUE - Removing the front item from the queue.
'''

# Queue() creates a new queue that is empty.
# It needs no parameters and returns an empty queue.
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):  # Tests to see whether the queue is empty.
        return not self.items   # It needs no parameters and returns a boolean value.

    def enqueue(self, item):    # Adds a new item to the rear of the queue.
        return self.items.append(item)  # It needs the item and returns nothing.

    def dequeue(self):  # Removes the front item from the queue.
        return None if self.isEmpty() else self.items.pop(0)    # It needs no parameters and returns the item. Queue is modified.

    def size(self): # Returns the number of items in the queue.
        return len(self.items)  # It needs no parameters and returns an integer value.

    def front(self):    # Returns the front item from the stack but does not remove it.
        return None if self.isEmpty else self.items[0]  # It needs no parameters. The stack is not modified.

    def rear(self): # Returns the rear item from the stack but does not remove it.
        return None if self.isEmpty else self.items[-1]    # It needs no parameters. The stack is not modified.