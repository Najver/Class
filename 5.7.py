class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingSinglyLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Cannot pop from an empty stack.")
        popped_data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def count(self):
        return self.size

    def clear(self):
        self.top = None
        self.size = 0

    def popAll(self):
        elements = []
        while self.top is not None:
            elements.append(self.pop())
        return elements

stack = StackUsingSinglyLinkedList()

stack.add(10)
stack.add(20)
stack.add(30)
stack.add(40)
stack.add(50)

print(stack.pop())
print(stack.count())

print(stack.popAll())
print(stack.count())

stack.clear()
print(stack.count())

