class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_Empty(self):
        return self.head is None
    
    def peek(self):
        if self.is_Empty():
            return "Stack is empty"
        return self.head.data
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head #if empty its just None
        self.head = new_node

    def pop(self):
        if self.is_Empty():
            return "Stack is empty"
        popped = self.head.data
        self.head = self.head.next
        return popped