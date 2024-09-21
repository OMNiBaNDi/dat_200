class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def is_Empty(self):
        return self.front is None
    
    def peek(self):
        if self.is_Empty():
            return "Queue is empty!"
        return self.front.data
        
    def enqueue(self, item):
        new_node = Node(item)
        if self.is_Empty():
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_Empty():
            return "Queue is empty!"
        
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

