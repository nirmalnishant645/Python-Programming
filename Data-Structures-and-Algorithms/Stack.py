'''
Last In First Out (LIFO)

Stacks can be used to reverse the order of items.

Example of stack in real world:
Web Browser Back Button:
As you navigate from web page to web page, those pages are placed on a stack (actually it is the URLs that are going in the stack).
The current page that you are viewing is on the top and the first page you looked at is at the base.
If you click on the Back Button, you begin to move in reverse order through pages.
'''

class Stack:
    #Initializing a list
    arr = []

    #To push an element into the Stack
    def push(self, item):
        self.arr.append(item)

    #To check if the stack is empty
    def isEmpty(self):
        return not self.arr

    #To pop the last element off the stack
    def pop(self):
        return None if self.isEmpty() else self.arr.pop()

    #To peek into the Stack
    def peek(self):
        return None if self.isEmpty() else self.arr[-1]


    #To display the whole Stack
    def display(self):
        print(self.arr)

x = Stack() #Creating an object of stack class
x.display()
print('Pushing 1 into the stack')
x.push('1')
x.display()
print('Pushing 2 into the stack')
x.push('2')
x.display()
print('Peeking into the top of the stack')
print(x.peek())
print('Popping the last element from the stack')
print(x.pop())
x.display()
print('Popping the last element from the stack')
print(x.pop())
x.display()
print('Checking if the stack is empty')
print(x.isEmpty())
print('Popping the stack even though it is empty')
print(x.pop())
