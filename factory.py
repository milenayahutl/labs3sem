#порождающий шаблон определяет интерфейс для создания объекта, но детали остаются на подклассах
from beverage import Cappuccino, Latte

class BeverageFactory:
    @staticmethod
    #декоратор, нужен чтобы в дальнейшем не создавать объект класса BeverageFactory, а вызывать ф-ию make напрямую
    def make(name):
        if name == "Cappuccino":
            return Cappuccino()
        elif name == "Latte":
            return Latte()
        else:
            raise NameError(f"Unknown drink: {name}")