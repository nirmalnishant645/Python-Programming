'''
DEQUE - DOUBLE ENDED QUEUE
New items can be added at either the front or the rear.
Existing items can be removed from either end.
Provides capabilities of stack and queue.
'''

# Deque() creates a new deque that is empty.
# It needs no parameters and returns an empty deque.
class Deque(object):
    
    def __init__(self):
        self.items = []

    def isEmpty(self):  # Tests to see whether the Deque is empty.
        return not self.items   # It needs no parameters and returns a boolean value.

    def addFront(self, item):   # Adds a new item to the font of the Deque.
        self.items.insert(0, item)  # It needs the item and returns nothing.

    def addRear(self, item):    # Adds a new item to the rear of the Deque.
        self.items.append(item) # It needs the item and returns nothing.

    def removeFront(self):  # Removes the front item from the Deque.
        return None if self.isEmpty() else self.items.pop(0)    # It needs no parameters and returns the item. Deque is modified.

    def removeRear(self):   # Removes the rear item from the Deque.
        return None if self.isEmpty() else self.items.pop() # It needs no parameters and returns the item. the Deque is modified.

    def size(self): # Returns the number of items in the Deque.
        return len(self.items)  # It needs no parameters and returns an integer.