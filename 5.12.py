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

# Testování
sto_korun = PenezniHotovost(100, "CZK")
dve_sta_korun = sto_korun + 100
print(sto_korun)  # 100 CZK
print(dve_sta_korun)  # 200 CZK

# Odečítání
sto_korun_mene = sto_korun - 50
print(sto_korun_mene)  # 50 CZK

# Násobení
dvaapulkrat = sto_korun * 2.5
print(dvaapulkrat)  # 250.0 CZK

# Mocnění
dva_koruny = sto_korun ** 2
print(dva_koruny)  # 10000 CZK
