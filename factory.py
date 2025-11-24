#порождающий шаблон создает объекты но не напрямую а через оющий интерфейс (функцию make)
from beverage import Cappuccino, Latte

class BeverageFactory:
    @staticmethod
    #декоратор, он нужен чтобы в дальнейшем не создавать объект BeverageFactory, а вызывать ф-ию make напрямую
    def make(name):
        if name == "Cappuccino":
            return Cappuccino()
        elif name == "Latte":
            return Latte()
        else:
            raise NameError(f"Unknown drink: {name}")