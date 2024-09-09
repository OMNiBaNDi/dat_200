


#Node class
class Node:
    #initiating the node object
    def __init__(self, data):
        self.data = data
        self.next = None


#Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
    
    #Traversal
    def traverse_and_print(self):
        temp = self.head

        while (temp != None):
            print(temp.data, end="")
            temp = temp.next
        print()

    #Insert new node at beginning
    def insert_front(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

    #Insert new node at the end
    def insert_end(self, new):
        new_node = Node(new)

        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = new_node


    #Isert new node at given position
    def insert_at(self, new, position):
        new_node = Node(new)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            count = 0
            while (temp != None and count < position):
                prev = temp
                temp = temp.next
                count += 1
            new_node.next = temp
            prev.next = new_node

    #Deleting first node
    def delete_front(self):
        if (self.head != None):
            temp = self.head
            self.head = temp.next
            temp = None
    

    #Deleting the last node of linked list
    def delete_last(self):
        temp = self.head
        while (temp.next.next != None):
            temp = temp.next
        temp.next = None
    
    #Delete a node at given position
    def delete_at(self, position):
        if position == 0:
            self.delete_front()
            return
        else:
            temp = self.head
            count = 0
            while (temp != None and count < position):
                prev = temp
                temp = temp.next
                count += 1
            prev.next = temp.next
    
    
    #Assignment 2
    def find_max_min(self):
        temp = self.head
        min = temp.data
        max = temp.data
        while (temp != None):
            if temp.data < min:
                min = temp.data
            elif temp.data > max:
                max = temp.data
            temp = temp.next
        print(f"Max is: {max}\nMin is: {min}")

MyList = LinkedList()

MyList.insert_front(5)
MyList.insert_front(4)
MyList.insert_front(3)
MyList.insert_front(2)
MyList.insert_front(1)
MyList.insert_front(6)

MyList.find_max_min()