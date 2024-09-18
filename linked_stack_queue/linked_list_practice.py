class Node:
    def __init_(self, data):
        data.self = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def traverse_and_print(self):
        temp = self.head
        while temp != None:
            print(temp)
            temp = temp.next
        print("finished traversing Linked List")

    def insert_front(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, new):
        new_node = Node(new)
        temp = self.head
        while temp != None:
            temp = temp.next
        temp.next = new_node

    def insert_at(self, new, pos):
        new_node = Node(new)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            count = 0
            while temp != None and count < pos:
                prev = temp
                temp = temp.next
                count += 1
            prev.next = new_node
            new_node.next = temp

    def delete_front(self):
        if self.head != None:
            temp = self.head
            self.head = temp.next
            temp = None
    
    def delete_back(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def delete_at(self, pos):
        if pos == 0:
            self.delete_front()
        else:
            count = 0
            temp = self.head
            while temp != None and count < pos:
                prev = temp
                temp = temp.next
                count += 1
            prev.next = temp.next
            

