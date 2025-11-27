from factory import BeverageFactory
from order import Order, Customer
from beverage import WhippedCream, ExtraEspresso, Cappuccino

#создаем напиток через фабрику (пораждающий)
drink = BeverageFactory.make("Cappuccino")

#допы (структурный)
drink = WhippedCream(drink) #создаем объект класса whippedcream
drink = ExtraEspresso(drink)

print("Drink: ", drink.get_description())
print("Price: ", drink.get_price())

order = Order("Drink-001", drink)

#добавляем клиента для отслеживания статуса заказа
milena = Customer("Milena")
order.subscribe(milena)

order.get_status("preparing")
order.get_status("ready")
