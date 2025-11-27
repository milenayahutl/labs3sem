from behave import given, when, then
from order import Order, Customer


@given('An order with ID "{order_id}" was created')
def step_impl(context, order_id):
    context.order = Order(order_id, beverage=None)


@given('client "{name}" subscribed to notifications')
def step_impl(context, name):
    context.customer = Customer(name)
    context.messages = []

    def fake_update(order):
        msg = f"{name}, order {order.order_id}: {order.status}!"
        context.messages.append(msg)

    context.customer.update = fake_update
    context.order.subscribe(context.customer)


@when('the order status changes to "{status}"')
def step_impl(context, status):
    context.order.get_status(status)


@then('"{name}" should see the message: "{expected_message}"')
def step_impl(context, name, expected_message):
    assert len(context.messages) > 0, "No messages!"
    actual_message = context.messages[-1]
    assert actual_message == expected_message, f"Expected:\n{expected_message}\nGot:\n{actual_message}"