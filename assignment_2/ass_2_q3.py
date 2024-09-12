class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    def remove(self, data):
        current = self.head
        while current is not None:
            if current.get_data() == data:
                if current == self.head:
                    self.head = current.get_next()
                    if self.head is not None:
                        self.head.set_prev(None)
                elif current == self.tail:
                    self.tail = current.get_prev()
                    if self.tail is not None:
                        self.tail.set_next(None)
                else:
                    current.get_prev().set_next(current.get_next())
                    current.get_next().set_prev(current.get_prev())
                return True
            current = current.get_next()
        return False

    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print()

    def display_backward(self):
        current = self.tail
        while current is not None:
            print(current.get_data(), end=" ")
            current = current.get_prev()
        print()

    def swap_k_nodes(self, k):
        if self.is_empty() or k <= 0:
            return

        # Find the length of the list
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.get_next()

        if k > length // 2:
            print("K is too large to swap")
            return

        # Find the first K nodes
        first_k_start = self.head
        first_k_end = self.head
        for _ in range(k - 1):
            first_k_end = first_k_end.get_next()

        # Find the last K nodes
        last_k_start = self.tail
        last_k_end = self.tail
        for _ in range(k - 1):
            last_k_end = last_k_end.get_prev()
        print(f"first_k_start: {first_k_start.data}, first_k_end: {first_k_end.data}, last_k_start: {last_k_start.data}, last_k_end: {last_k_end.data}")
        # Swap the first K nodes with the last K nodes
        for _ in range(k):
            # Swap the nodes
            first_k_start.data, last_k_start.data = last_k_start.data, first_k_start.data
            first_k_start = first_k_start.get_next()
            last_k_start = last_k_start.get_prev()


# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(7)
dll.append(8)

print("List before swapping:")
dll.display_forward()

k = 2
dll.swap_k_nodes(k)

print("List after swapping first k nodes with last k nodes:")
dll.display_forward()