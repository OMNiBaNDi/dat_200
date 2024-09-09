

#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#Doubly linked list class
class LinkedList:
    def __init__(self):
        self.head = None