#наблюдатель (уведы о заказе)
#поведенческий шаблон управляет коммуникацией м/у объектами


class Order:
    def __init__(self, order_id, beverage):
        self.order_id = order_id
        self.beverage = beverage
        self.status = "created"
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    #используется только внутри класса, а не снаружи
    def _notify(self):
        for observer in self.observers:
            observer.update(self)

    def get_status(self, new_status):
        self.status = new_status
        self._notify() #когда статус меняется, уведомляем пользователя

class Customer:
    def __init__(self, name):
        self.name = name

    def update(self, order):
        print(f"{self.name}, order {order.order_id}: {order.status}!")