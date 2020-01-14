class stack:
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

x = stack() #Creating an object of stack class
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
