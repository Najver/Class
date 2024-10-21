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
        if not self.head:
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

    def __contains__(self, item):
        """ Zjistí, zda se prvek nachází v seznamu. """
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

# Testování
fronta = Fronta()
fronta.add("Pepa")
fronta.add(2)
fronta.add(3)

if "Pepa" in fronta:
    print("Pepa je v seznamu")  # Tohle by mělo vytisknout tuto zprávu.
else:
    print("Pepa není v seznamu")

if 2 in fronta:
    print("2 je v seznamu")      # Tohle by mělo vytisknout tuto zprávu.

if 4 in fronta:
    print("4 je v seznamu")      # Tohle by se nemělo vytisknout.
else:
    print("4 není v seznamu")    # Tohle by mělo vytisknout tuto zprávu.
