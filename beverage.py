# прикол структурного шаблона в том что у нас есть базовый класс (родитель),
# нет нужны создавать новый класс для кофе с молоком или со сливками,
# достаточно создать декораторы, как бы опции, для изменения класса с тем же кофе


#создаем базовый класс для напитков и всякого ^.''.^
class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_description(self):
        return self.name
    def get_price(self):
        return self.price

class Cappuccino(Beverage):
    def __init__(self):
        super().__init__("Cappuccino", 2.0)   #super - функция для обращения к классу от которого наследуем

class Latte(Beverage):
    def __init__(self):
        super().__init__("Latte", 3.0)

#декораторы (допы) к напиткам, "оборачивают" напиток и добавляют опции
class ExtraEspresso:
    def __init__(self, beverage):
        self.beverage = beverage
    def get_description(self):
        return self.beverage.get_description() + ", double Espresso"
    def get_price(self):
        return self.beverage.get_price() + 0.5

class WhippedCream:
    def __init__(self, beverage):
        self.beverage = beverage
    def get_description(self):
        return self.beverage.get_description() + ", with whipped cream"
    def get_price(self):
        return self.beverage.get_price() + 0.3