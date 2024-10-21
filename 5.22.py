class Obdelnik:
    def __init__(self, delka: float, sirka: float):
        self._delka = 0
        self._sirka = 0
        self.delka = delka  # Využití setteru
        self.sirka = sirka  # Využití setteru

    @property
    def delka(self):
        return self._delka

    @delka.setter
    def delka(self, hodnota: float):
        if hodnota < 0:
            raise ValueError("Délka nesmí být záporná")
        self._delka = hodnota

    @property
    def sirka(self):
        return self._sirka

    @sirka.setter
    def sirka(self, hodnota: float):
        if hodnota < 0:
            raise ValueError("Šířka nesmí být záporná")
        self._sirka = hodnota

    def plocha(self):
        return self._delka * self._sirka

# Testovací kód
obdelnik = Obdelnik(5, 3)
print("Délka:", obdelnik.delka)  # 5
print("Šířka:", obdelnik.sirka)   # 3
print("Plocha:", obdelnik.plocha())  # 15

# Testování záporné hodnoty
try:
    obdelnik.delka = -2  # Mělo by vyhodit výjimku
except ValueError as e:
    print(e)  # Délka nesmí být záporná

try:
    obdelnik.sirka = -4  # Mělo by vyhodit výjimku
except ValueError as e:
    print(e)  # Šířka nesmí být záporná
