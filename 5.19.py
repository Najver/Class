class Firma:
    """ Třída reprezentuje firmu"""

    @staticmethod
    def factory_from_obchodni_nazev(obchodni_nazev: str):
        """
        Statická metoda vytvoří firmu z obchodního názvu.

        :param obchodni_nazev: Například "Česká spořitelna, a.s."
        :return: Nový objekt třídy Firma
        """
        # Rozdělení obchodního názvu na část názvu firmy a právní formu
        parts = obchodni_nazev.split(', ')

        if len(parts) != 2:
            raise Exception("Nelze parsovat obchodní název")

        nazev = parts[0]
        pravni_forma = parts[1]

        return Firma(nazev, pravni_forma)

    def __init__(self, nazev: str, pravni_forma: str):
        """
        Vytvoří instanci firmy.
        :param nazev: Název například "Maso a uzeniny od Pavlíka".
        :param pravni_forma: Právní forma, například "s.r.o" nebo "a.s." apod.
        """
        self.jmeno = nazev
        self.pravni_forma = pravni_forma


# Testovací kód
sporka = Firma.factory_from_obchodni_nazev("Česká spořitelna, a.s.")
print(sporka.pravni_forma)  # má vypsat "a.s."
