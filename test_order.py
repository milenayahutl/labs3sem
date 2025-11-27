from unittest.mock import Mock
from order import Order, Customer

def test_order_notification():
    order = Order("Test-001", None)
    customer = Customer("testik")
    customer.update = Mock()

    order.subscribe(customer)
    order.get_status("ready")

    customer.update.assert_called_once()
    print("Mock test passed!")

if __name__ == '__main__':
    test_order_notification()
    print("Test passed!")