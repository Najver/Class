class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class QueueUsingDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.head is None:
            raise IndexError("Cannot pop from an empty queue.")
        popped_data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return popped_data

    def count(self):
        return self.size

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def popAll(self):
        elements = []
        while self.head is not None:
            elements.append(self.pop())
        return elements

queue = QueueUsingDoublyLinkedList()

queue.add(10)
queue.add(20)
queue.add(30)
queue.add(40)
queue.add(50)

print(queue.pop())
print(queue.count())

print(queue.popAll())
print(queue.count())

queue.clear()
print(queue.count())
