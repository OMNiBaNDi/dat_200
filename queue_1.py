#Queue is a FIFO data structure.

"""
#Implementation of queue with arrays
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            return "Queue is empty!"
        
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return "Queue is empty"
        
    def isEmpty(self):
        return len(self.queue) == 0
"""

#Implementation of Queue with Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node

    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if not self.isEmpty():
            return self.front.data
        else:
            return "queue is empty"