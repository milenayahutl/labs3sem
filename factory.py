#порождающий шаблон
from beverage import Cappuccino, Latte

class BeverageFactory:
    @staticmethod
    def make(name):
        if name == "Cappuccino":
            return Cappuccino()
        elif name == "Latte":
            return Latte()
        else:
            raise NameError(f"Unknown drink: {name}")