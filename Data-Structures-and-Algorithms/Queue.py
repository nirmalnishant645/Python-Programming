'''
FIRST IN FIRST OUT (FIFO)
ENQUEUE - Adding a new item to the rear of the queue.
DEQUEUE - Removing the front item from the queue.
'''

class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return None if self.isEmpty() else self.items.pop(0)

    def size(self):
        return len(self.items)

    def front(self):
        return None if self.isEmpty else self.items[0]

    def rear(self):
        return None if self.isEmplty else self.items[-1]