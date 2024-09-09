

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new):
        new_node = Node(new)
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
    
    def remove_duplicates(self):
        if self.head == None:
            return
        
        current = self.head
        seen = set()
        while True:
            if current.data in seen:
                current.prev.next = current.next
                current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
            else:
                seen.add(current.data)

            current = current.next
            if current == self.head:
                break
    
    def display(self):
        if self.head == None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage
MyList = CircularDoublyLinkedList()
MyList.append(4)
MyList.append(4)
MyList.append(4)
MyList.append(4)
MyList.append(6)
MyList.append(8)
MyList.append(8)
MyList.append(12)
MyList.append(12)
MyList.append(12)

# Display the list before removing duplicates
print("List before removing duplicates:")
MyList.display()

# Remove duplicates
MyList.remove_duplicates()

# Display the list after removing duplicates
print("List after removing duplicates:")
MyList.display()