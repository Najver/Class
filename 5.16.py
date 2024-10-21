class Node:
    """ Třída představující uzel spojového seznamu. """
    def __init__(self, data):
        self.data = data
        self.next = None


class Fronta:
    """ Třída představující frontu jako jednosměrný spojový seznam. """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        """ Přidá prvek na konec fronty. """
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def pop(self):
        """ Odebere prvek z začátku fronty a vrátí jeho hodnotu. """
        if not self.head:
            raise Exception("Fronta je prázdná.")
        popped_value = self.head.data
        self.head = self.head.next
        if not self.head:  # Pokud je fronta prázdná, resetuj tail.
            self.tail = None
        self.size -= 1
        return popped_value

    def __len__(self):
        """ Vrátí počet prvků ve frontě. """
        return self.size

    def __getitem__(self, key):
        """ Vrátí prvek na dané pozici (indexu) ve frontě. """
        if key < 0 or key >= self.size:
            raise IndexError("Index mimo rozsah.")
        current = self.head
        for _ in range(key):
            current = current.next
        return current.data

    def __setitem__(self, key, value):
        """ Nastaví prvek na dané pozici (indexu) ve frontě. """
        if key < 0 or key >= self.size:
            raise IndexError("Index mimo rozsah.")
        current = self.head
        for _ in range(key):
            current = current.next
        current.data = value

# Testování
fronta = Fronta()
fronta.add(1)
fronta.add(2)
fronta.add(3)

print(len(fronta))         # Mělo by vrátit 3
print(fronta[0])          # Mělo by vrátit 1
print(fronta[1])          # Mělo by vrátit 2
print(fronta[2])          # Mělo by vrátit 3

fronta[0] = "Pepa"
print(fronta[0])          # Mělo by vrátit "Pepa"

fronta.pop()              # Odebere 1
print(len(fronta))        # Mělo by vrátit 2
