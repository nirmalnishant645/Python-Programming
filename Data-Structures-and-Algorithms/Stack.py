#Initializing an empty list
stack = []

#To push an element into the stack
def push(item):
    stack.append(item)

#Popping out the last element
def pops():
    return stack.pop() if len(stack) > 0 else None

#Printing the stack
def display():
    print(stack)


display()
print('Pushing 1 into stack')
push(1)
display()
print('Pushing 2 into stack')
push(2)
display()
print('Popping out the last element from the stack')
pops()
display()
print('Popping out the last element from the stack')
pops()
display()
print('Popping out an element even though the stack is empty')
pops()
display()
