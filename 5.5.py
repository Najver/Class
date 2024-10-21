class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data)
            last = current
            current = current.next
        return last

    def display_backward(self, last):
        current = last
        while current:
            print(current.data)
            current = current.prev

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

last_node = dll.display_forward()

dll.display_backward(last_node)
