import re

class PenezniHotovost:
    """
    Trida reprezentuje penezni hotovost v urcite mene
    """

    def __init__(self, castka: float, mena: str):
        """
        Pri vytvoreni tridy se musi specifikovat castka a mena, nebo se pouzije defaultnich 0 EUR

        :param castka: Jakekoli realne cislo, muze byt i zaporne
        :param mena: Mena vyjadrena jako tripismeny kod
        """
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._mena = mena
        self._castka = castka

    def __str__(self):
        """
        Vrati castku a menu jako string
        :return: <castka> <mena>
        """
        return str(self._castka) + " " + self._mena

    def __add__(self, other):
        """
        Pretizeni operatoru + ktere vytvori novy objekt jako vysledek operace scitani
        :param other: Lze scitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if isinstance(other, float) or isinstance(other, int):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other
            return vysledek

        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int, float a hotovosti ve stejne mene")

    def __sub__(self, other):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace odecteni
        :param other: Lze odečítat čísla typy int, float nebo jiný objekt peněžní hotovosti ve stejné měně
        :return: Vrací nový objekt s měnou podle původních objektů a zůstatkem jako výsledek operace odčítání
        """
        if isinstance(other, float) or isinstance(other, int):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other
            return vysledek

        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other._castka
            return vysledek

        raise Exception("Penezni hotovost lze odecitat pouze s int, float a hotovosti ve stejne mene")

    def __mul__(self, other):
        """
        Pretizeni operatoru * ktere vytvori novy objekt jako vysledek operace nasobeni
        :param other: Lze násobit čísla typy int, float
        :return: Vrací nový objekt s měnou podle původních objektů a zůstatkem jako výsledek operace násobení
        """
        if isinstance(other, float) or isinstance(other, int):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other
            return vysledek

        raise Exception("Penezni hotovost lze nasobit pouze s int nebo float")

    def __pow__(self, power, modulo=None):
        """
        Pretizeni operatoru ** ktere vytvori novy objekt jako vysledek operace mocneni
        :param power: Exponent, který musí být celé číslo
        :param modulo: Nepovinný argument pro modulo, může být None nebo celé číslo
        :return: Vrací nový objekt s měnou podle původních objektů a zůstatkem jako výsledek operace mocnění
        """
        if not isinstance(power, int):
            raise Exception("Exponent musí být celé číslo")

        vysledek = PenezniHotovost(0, self._mena)
        vysledek._castka = self._castka ** power

        if modulo is not None:
            vysledek._castka %= modulo

        return vysledek

    def __iadd__(self, other):
        """
        Implementace operátoru +=, který upraví aktuální objekt
        :param other: Lze přičíst čísla typu int, float nebo jiný objekt peněžní hotovosti ve stejné měně
        :return: Vrací aktuální objekt po úpravě
        """
        if isinstance(other, float) or isinstance(other, int):
            self._castka += other
            return self

        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka += other._castka
            return self

        raise Exception("Penezni hotovost lze přičítat pouze s int, float a hotovosti ve stejné měně")

    def __isub__(self, other):
        """
        Implementace operátoru -=, který upraví aktuální objekt
        :param other: Lze odečítat čísla typy int, float nebo jiný objekt peněžní hotovosti ve stejné měně
        :return: Vrací aktuální objekt po úpravě
        """
        if isinstance(other, float) or isinstance(other, int):
            self._castka -= other
            return self

        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka -= other._castka
            return self

        raise Exception("Penezni hotovost lze odečítat pouze s int, float a hotovosti ve stejné měně")

    def __imul__(self, other):
        """
        Implementace operátoru *=, který upraví aktuální objekt
        :param other: Lze násobit čísla typy int, float
        :return: Vrací aktuální objekt po úpravě
        """
        if isinstance(other, float) or isinstance(other, int):
            self._castka *= other
            return self

        raise Exception("Penezni hotovost lze násobit pouze s int nebo float")

    def __itruediv__(self, other):
        """
        Implementace operátoru /=, který upraví aktuální objekt
        :param other: Lze dělit čísla typy int, float nebo jiný objekt peněžní hotovosti
        :return: Vrací aktuální objekt po úpravě
        """
        if isinstance(other, float) or isinstance(other, int):
            self._castka /= other
            return self

        if isinstance(other, PenezniHotovost) and other._mena == self._mena:
            self._castka /= other._castka
            return self

        raise Exception("Penezni hotovost lze dělit pouze s int, float a hotovosti ve stejné měně")


# Testování
vyplata = PenezniHotovost(1000, "CZK")
vyplata += 2000  # 1000 + 2000 = 3000
vyplata -= 500   # 3000 - 500 = 2500
vyplata *= 2     # 2500 * 2 = 5000
print(vyplata)   # má vypsat 5000

vyplata /= 2
print(vyplata)  # 2500.0 CZK
