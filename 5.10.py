class Zbozi:
    def __new__(cls, nazev, cena):
        if not nazev or not isinstance(cena, (int, float)) or cena < 0:
            instance = None
        else:
            instance = super().__new__(cls)

        return instance

    def __init__(self, nazev, cena):
        if self is not None:
            self.nazev = nazev
            self.cena = cena

a = Zbozi("Rohlik", 5)
b = Zbozi("", 10)
c = Zbozi("Hackers item", -10)
d = Zbozi("Item with non-numeric price", "ten")

print(a)
print(b)
print(c)
print(d)