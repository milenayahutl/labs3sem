from unittest.mock import Mock
from order import Order, Customer

def test_order_notification():
    order = Order("Test-001", None)
    customer = Customer("testik")
    customer.update = Mock()   #заменяет на фейк объект

    order.subscribe(customer)
    order.get_status("ready")

    customer.update.assert_called_once() #успех если вызов был 1 раз
    print("Mock test passed!")

if __name__ == '__main__':
    test_order_notification()
    print("Test passed!")