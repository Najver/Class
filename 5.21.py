class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

# Testovací kód
a = Singleton()
b = Singleton()

print(a is b)  # Musí vypsat True

a.moje_nova_promenna_pro_a = "Test"
print(a.moje_nova_promenna_pro_a)  # Musí vypsat "Test"
print(b.moje_nova_promenna_pro_a)  # Musí vypsat také "Test"
