class KonfiguraceKonference:
    _maximalni_pocet_ucastniku = 0

    @classmethod
    def set_maximalni_pocet_ucastniku(cls, max):
        cls._maximalni_pocet_ucastniku = max

    @classmethod
    def get_maximalni_pocet_ucastniku(cls):
        return cls._maximalni_pocet_ucastniku

    def __new__(cls, *args, **kwargs):
        raise Exception("Nelze vytvářet instance třídy KonfiguraceKonference.")

# Testovací kód
print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

KonfiguraceKonference.set_maximalni_pocet_ucastniku(212)
print(KonfiguraceKonference.get_maximalni_pocet_ucastniku())

# Pokus o vytvoření instance by měl vyhodit výjimku
try:
    mojeKonfigurace = KonfiguraceKonference()
except Exception as e:
    print(e)  # Mělo by vypsat: Nelze vytvářet instance třídy KonfiguraceKonference.
