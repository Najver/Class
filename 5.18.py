class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        return current.data

    def __setitem__(self, index, value):
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next
        if current is None:
            raise IndexError("Index out of range")
        current.data = value

# Příklad použití
seznam = SinglyLinkedList()
seznam.append("Pepa")
seznam.append("Karel")
seznam.append("Mirka")

for prvek in seznam:
    print(prvek)

if "Pepa" in seznam:
    print("Pepa je v seznamu")

print(len(seznam))
print(seznam[1])  # vrátí "Karel"
seznam[0] = "Nový Pepa"
print(seznam[0])  # vrátí "Nový Pepa"
