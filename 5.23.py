class Zbozi:

    def __init__(self, nazev):
        self.nazev = nazev

    def __del__(self):
        print("Zbozi " + str(self.nazev) + " bylo vymazano z pameti")

# Experiment 1: Vytvoření a smazání zboží
z = Zbozi("Jablko")
del z

# Experiment 2: Odstranění příkazu del
z = Zbozi("Hruška")
print("Konec programu")  # Vytiskne "Konec programu", zboží bude smazáno po ukončení programu

# Experiment 3: Odkaz na stejné zboží
z = Zbozi("Banán")
me_oblibene_zbozi = z
del z  # Smaže pouze odkaz z, zboží zůstává v paměti kvůli odkazu me_oblibene_zbozi
