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

#Implementation of circular queue with arrays
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        
        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"Enqueued {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        removed_item = self.queue[self.front]
        if self.front == self.rear: #queue only has one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Dequeued {removed_item}")

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue elements are: ", end=" ")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
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
        self.rear = new_node

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
    
    def isEmpty(self):
        return self.front is None