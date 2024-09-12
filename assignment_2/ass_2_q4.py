from datetime import datetime

class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False
        self.next = None
        self.prev = None

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task(description={self.description}, priority={self.priority}, due_date={self.due_date}, completed={self.completed})"


class ToDoList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_task(self, description, priority, due_date):
        new_task = Task(description, priority, due_date)
        if self.is_empty():
            self.head = new_task
            self.tail = new_task
        else:
            self.tail.next = new_task
            new_task.prev = self.tail
            self.tail = new_task

    def delete_task(self, description):
        current = self.head
        while current is not None:
            if current.description == description:
                if current == self.head:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def display_tasks(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next

    def mark_task_completed(self, description):
        current = self.head
        while current is not None:
            if current.description == description:
                current.mark_completed()
                return True
            current = current.next
        return False


# Example usage
todo_list = ToDoList()
todo_list.add_task("Buy groceries", 1, datetime(2023, 10, 10))
todo_list.add_task("Complete assignment", 2, datetime(2023, 10, 12))
todo_list.add_task("Pay bills", 1, datetime(2023, 10, 15))

print("Tasks before marking as completed:")
todo_list.display_tasks()

todo_list.mark_task_completed("Complete assignment")

print("\nTasks after marking 'Complete assignment' as completed:")
todo_list.display_tasks()

todo_list.delete_task("Buy groceries")

print("\nTasks after deleting 'Buy groceries':")
todo_list.display_tasks()