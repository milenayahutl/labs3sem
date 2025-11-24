from factory import BeverageFactory
from order import Order, Customer
from beverage import WhippedCream, ExtraEspresso, Cappuccino

#создаем напиток через фабрику (пораждающий)
drink = BeverageFactory.make("Cappuccino")

#допы (структурный)
drink = WhippedCream(drink)
drink = ExtraEspresso(drink)

print("Drink: ", drink.get_description())
print("Price: ", drink.get_price())

#создаем заказ
order = Order("Drink-001", drink)

#добавляем клиента для отслеживания статуса заказа (поведенческий)
milena = Customer("Milena")
order.subscribe(milena)

#меняем статус заказа
order.get_status("preparing")
order.get_status("ready")
