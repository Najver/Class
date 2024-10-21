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
        """
        Metoda zjistí, jestli je zboží menší než druhé zboží. Porovnává se pouze váha.
        :param other: Třída pro porovnání, musí to být instance Zbozi
        :return: True pokud je self menší než other
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')

        return self._vaha < other._vaha

    def __gt__(self, other):
        """
        Metoda zjistí, jestli je zboží větší než druhé zboží. Porovnává se pouze váha.
        :param other: Třída pro porovnání, musí to být instance Zbozi
        :return: True pokud je self větší než other
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')

        return self._vaha > other._vaha

    def __le__(self, other):
        """
        Metoda zjistí, jestli je zboží menší nebo rovno druhému zboží. Porovnává se pouze váha.
        :param other: Třída pro porovnání, musí to být instance Zbozi
        :return: True pokud je self menší nebo rovno other
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')

        return self._vaha <= other._vaha

    def __ge__(self, other):
        """
        Metoda zjistí, jestli je zboží větší nebo rovno druhému zboží. Porovnává se pouze váha.
        :param other: Třída pro porovnání, musí to být instance Zbozi
        :return: True pokud je self větší nebo rovno other
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')

        return self._vaha >= other._vaha

    def __eq__(self, other):
        """
        Metoda zjistí, jestli jsou dvě zboží stejná (mají stejnou váhu).
        :param other: Třída pro porovnání, musí to být instance Zbozi
        :return: True pokud jsou self a other stejné
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')

        return self._vaha == other._vaha

    def __ne__(self, other):
        """
        Metoda zjistí, jestli jsou dvě zboží různá (mají různou váhu).
        :param other: Třída pro porovnání, musí to být instance Zbozi
        :return: True pokud jsou self a other různé
        """
        if not isinstance(other, Zbozi):
            raise Exception('Porovnávat lze jen zboží mezi sebou')

        return self._vaha != other._vaha


# Testování
kilo_brambor = Zbozi("Bramobra", 1)
krabice_mleka = Zbozi("Mleko", 1.029)

if kilo_brambor < krabice_mleka:
    print("Kilo brambor je lehčí než krabice mléka.")

if kilo_brambor > krabice_mleka:
    print("Kilo brambor je těžší než krabice mléka.")
else:
    print("Kilo brambor není těžší než krabice mléka.")

if kilo_brambor <= krabice_mleka:
    print("Kilo brambor je buď lehčí, nebo stejně těžké jako krabice mléka.")

if kilo_brambor >= krabice_mleka:
    print("Kilo brambor je buď těžší, nebo stejně těžké jako krabice mléka.")

if kilo_brambor == krabice_mleka:
    print("Kilo brambor a krabice mléka mají stejnou váhu.")
else:
    print("Kilo brambor a krabice mléka nemají stejnou váhu.")

if kilo_brambor != krabice_mleka:
    print("Kilo brambor a krabice mléka jsou různé.")
