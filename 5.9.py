class Auto:
    """ Třída auto reprezentuje auto pro simulaci reálného vozidla pro cvičení PV na SPSE Jecna """

    def __init__(self, objem_nadrze_l: float, spotreba_na_100_km_l: float):
        """
        Konstruktor nastaví objem nádrže a spotřebu dle parametrů a nastaví prázdnou nádrž a najeté kilometry na 0.

        :param objem_nadrze_l: Objem nádrže v litrech
        :param spotreba_na_100_km_l: Spotřeba na 100 km v litrech
        """
        if objem_nadrze_l < 0:
            raise Exception("Nádrž musí mít kladný objem")
        if spotreba_na_100_km_l < 0:
            raise Exception("Spotřeba nesmí být záporná")

        self.objem_nadrze_l = objem_nadrze_l
        self.spotreba_na_100_km_l = spotreba_na_100_km_l
        self._aktualni_objem_paliva_v_nadrzi_l = 0
        self._najete_km = 0

    def aktualni_stav_nadrze(self) -> float:
        """
        Metoda vrátí aktuální stav nádrže.

        :return: Zbylé palivo v nádrži v litrech
        """
        return self._aktualni_objem_paliva_v_nadrzi_l

    def natankuj(self, objem_l: float) -> None:
        """
        Naplní nádrž palivem.

        :param objem_l: Objem paliva, který má být naložen do nádrže v litrech
        :return: None
        """
        if objem_l < 0:
            raise Exception("Nelze odčerpat palivo pomocí metody natankovat")

        if (self._aktualni_objem_paliva_v_nadrzi_l + objem_l) > self.objem_nadrze_l:
            raise Exception("Nelze načerpat více než je kapacita nádrže")

        self._aktualni_objem_paliva_v_nadrzi_l += objem_l

    def popojed(self, pocet_km: float) -> None:
        """
        Přejede daný počet kilometrů a odečte potřebné palivo z nádrže.

        :param pocet_km: Počet kilometrů, které auto ujede
        :return: None
        """
        if pocet_km < 0:
            raise Exception("Couvání je také jízda, směr neřešíme")

        spotreba_paliva_l = pocet_km / 100.0 * self.spotreba_na_100_km_l

        if self._aktualni_objem_paliva_v_nadrzi_l < spotreba_paliva_l:
            raise Exception("Na jízdu není dostatek paliva")

        self._aktualni_objem_paliva_v_nadrzi_l -= spotreba_paliva_l
        self._najete_km += pocet_km

    def aktualni_stav_najetych_km(self) -> float:
        """
        Vrací aktuální počet najetých kilometrů.

        :return: Najeté kilometry
        """
        return self._najete_km
