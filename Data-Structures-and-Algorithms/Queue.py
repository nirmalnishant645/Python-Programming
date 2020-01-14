class Queue:
    #Initializing list
    arr = []

    #Add an item into the queue
    def enqueue(self, item):
        self.arr.append(item)

    #To check if the queue is empty
    def isEmpty(self):
        return not self.arr

    #Remove an item from the queue
    def dequeue(self):
        return None if self.isEmpty() else self.arr.pop(0)

    #Get the front item of the Queue
    def front(self):
        return self.arr[0]

    #Get the last item from the queue
    def rear(self):
        return self.arr[-1]

    #To display the whole Stack
    def display(self):
        print(self.arr)

x = Queue() #Creating an object of queue class
x.display()
print('Enquing 1 into queue')
x.enqueue('1')
x.display()
print('Enquing 1 into queue')
x.enqueue('2')
x.display()
print('Peeking the front item of the queue')
print(x.front())
print('Peeking the rear item of the queue')
print(x.rear())
print('Dequing an item from the queue')
print(x.dequeue())
x.display()
print('Dequing an item from the queue')
print(x.dequeue())
x.display()
print('Checking if the queue is empty')
print(x.isEmpty())
print('Dequing an item from the queue even though the queue is empty')
print(x.dequeue())
