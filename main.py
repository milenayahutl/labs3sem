from factory import BeverageFactory
from order import Order, Customer
from beverage import WhippedCream, ExtraEspresso, Cappuccino

drink = BeverageFactory.make("Cappuccino")

drink = WhippedCream(drink)
drink = ExtraEspresso(drink)

print("Drink: ", drink.get_description())
print("Price: ", drink.get_price())

order = Order("Drink-001", drink)

milena = Customer("Milena")
order.subscribe(milena)

order.get_status("preparing")
order.get_status("ready")
