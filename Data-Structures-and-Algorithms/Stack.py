'''
Last In First Out (LIFO)

Stacks can be used to reverse the order of items.

Example of stack in real world:
Web Browser Back Button:
As you navigate from web page to web page, those pages are placed on a stack (actually it is the URLs that are going in the stack).
The current page that you are viewing is on the top and the first page you looked at is at the base.
If you click on the Back Button, you begin to move in reverse order through pages.
'''

# Stack() creates a new stack that is empty.
# It needs no parameters and returns an empty stack.
class Stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):  # Tests to see whether the stack is empty.
        return not self.items   # It needs no parameters and returns an integer.

    def push(self, item):   # Adds a new item to the top of the stack.
        self.items.append(item) # It needs the item and returns nothing.

    def pop(self):  # Removes the top item from the stack.
        return None if self.isEmpty else self.items.pop() # It needs no parameters and returns the item. Stack is modified.

    def peek(self): # Returns the top item from the stack but does not remove it.
        return None if self.isEmpty() else self.items[-1]  # It needs no parameters. The stack is not modified.

    def size(self): # Returns the number of items on the stack.
        return len(self.items)  # It needs no parameters and returns an integer.