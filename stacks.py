#Stack is a LIFO(Last In First Out) data structure. Basic operations: Push(), Pop(), Peek/Top(), isEmpty(), isFull()

"""
#Implementation using array
class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        if(len(self.stack) == 0):
            print("Stack is empty!")
        else:
            print("Stack is not empty!")

    def push(self, item):
        self.stack.append(item)
        print(item, "is added to the stack")

    def pop(self):
        if (len(self.stack) == 0):
            print("error")
        else:
            print(self.stack.pop(), "is deleted from the stack.")

    def peek(self):
        if(len(self.stack) == 0):
            print("stack is empty")
            return -1
        else:
            return self.stack[-1]
"""

#Stack Implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if not self.isEmpty():
            popped = self.head.data
            self.head = self.head.next
            return popped
        else:
            return "Stack is empty!"
        
    def peek(self):
        if not self.isEmpty():
            return self.head.data
        else:
            return "Stack is empty"
        
    def isEmpty(self):
        return self.head is None