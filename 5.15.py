import re

class Zbozi:
    """ Třída zboží pro ukázku příkladu relacních operátorů"""

    def __init__(self, nazev: str, vaha: float):
        """
        Při vytvoření se nastavuje název zboží a jeho váha
        :param nazev: Název musí být znaky v rozsahu 1 až 200 znaků
        :param vaha: Váha musí být kladné a nenulové číslo
        """
        if not re.match(r"^[\D ]{1,200}$", nazev):
            raise Exception('Název musí být v rozsahu 1 až 200 znaků')
        if vaha <= 0:
            raise Exception('Váha nesmí být záporná nebo nula')

        self._nazev = nazev
        self._vaha = vaha

    def __lt__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')
        return self._vaha < other._vaha

    def __gt__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')
        return self._vaha > other._vaha

    def __le__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')
        return self._vaha <= other._vaha

    def __ge__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')
        return self._vaha >= other._vaha

    def __eq__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')
        return self._nazev == other._nazev and self._vaha == other._vaha

    def __ne__(self, other):
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')
        return not self.__eq__(other)

    def __hash__(self):
        """
        Vytváří unikátní hash na základě názvu a váhy zboží.
        :return: Unikátní hash jako celé číslo
        """
        return hash((self._nazev, self._vaha))

    def __str__(self):
        return f"{self._nazev}, {self._vaha} kg"


# Testování
zbozi1 = Zbozi("Mrkev", 1)
print(hash(zbozi1))

zbozi2 = Zbozi("Mrkev", 1)
zbozi3 = Zbozi("Celer", 1)

x = set()
x.add(zbozi1)
x.add(zbozi2)
x.add(zbozi3)

print(len(x))  # Očekávaný výstup: 2
