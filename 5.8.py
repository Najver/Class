class Auto:
    """ Trida auto reprezentuje auto pro simulaci realneho vozidlo pro cviceni PV na SPSE Jecna """

    def __init__(self, objem_nadrze_l : float, spotreba_na_100_km_l : float):
        """
        Konstruktor nastavi objem nadrze a spotrebu dle parametru a nastavi prazdnou nadrz.

        :param objem_nadrze_l: Objem nadrze v litrech
        :param spotreba_na_100_km_l: Spotreba na 100km v litrech
        """

        if objem_nadrze_l < 0:
            raise Exception("Nadrz musi mit kladny objem")
        if spotreba_na_100_km_l < 0:
            raise Exception("Spotreba nesmi byt zaporna")

        self.objem_nadrze_l = objem_nadrze_l
        self.spotreba_na_100_km_l = spotreba_na_100_km_l
        self._aktualni_objem_paliva_v_nadrzi_l = 0

    def aktualni_stav_nadrze(self) -> float:
        """
        Metoda vrati aktualni stav nadrze

        :return: Zbyle palivo v nadrzi v litrech
        """
        return self._aktualni_objem_paliva_v_nadrzi_l

    def natankuj(self, objem_l : float ) -> None:
        if objem_l < 0:
            raise Exception("Nelze odcerpat palivo pomoci metody natankovat")

        if (self._aktualni_objem_paliva_v_nadrzi_l + objem_l) > self.objem_nadrze_l:
            raise Exception("Nelze nacerpat vice nez je kapacita nadrze")

        self._aktualni_objem_paliva_v_nadrzi_l += objem_l

    def popojed(self, pocet_km : float ) -> None:
        if pocet_km < 0:
            raise Exception("Couvani je take jizda, smer neresime")

        spotreba_paliva_l = pocet_km/100.0 * self.spotreba_na_100_km_l

        if self._aktualni_objem_paliva_v_nadrzi_l < spotreba_paliva_l:
            raise Exception("Na jizdu neni dostatek paliva")

        self._aktualni_objem_paliva_v_nadrzi_l -= spotreba_paliva_l
auto = Auto(objem_nadrze_l=30, spotreba_na_100_km_l=12.5)
auto.natankuj(22.5)
auto.popojed(20)

print(f"Aktualni stav nadrze: {auto.aktualni_stav_nadrze()} l")
#Jaké jsou atributy/vlastnosti třídy?
#Atributy třídy zahrnují celkový objem nádrže (objem_nadrze_l), spotřebu paliva na 100 km (spotreba_na_100_km_l) a aktuální stav paliva v nádrži (_aktualni_objem_paliva_v_nadrzi_l).

#Jaké atributy/vlastnosti třídy jsou public a jaké private?
#Public atributy jsou objem_nadrze_l a spotreba_na_100_km_l, protože jsou přímo přístupné. Private atribut je _aktualni_objem_paliva_v_nadrzi_l, který je označen jako privátní a není přístupný zvenčí.

#Jak je řešen ve třídě princip zapouzdření, jak se manipuluje s private atributy?
#Princip zapouzdření je řešen pomocí metod, které umožňují manipulaci s privátním atributem. Například metoda aktualni_stav_nadrze() vrací aktuální stav paliva, a metody natankuj() a popojed() umožňují bezpečné přidávání a odebírání paliva bez přímého přístupu k privátnímu atributu.