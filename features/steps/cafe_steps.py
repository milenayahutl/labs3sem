from behave import given, when, then
from beverage import Cappuccino, WhippedCream

#подготовка
@given('i have cappuccino')
def step_impl(context):
    context.drink = Cappuccino()

#действие
@when('i add whipped cream')
def step_impl(context):
    context.drink = WhippedCream(context.drink)

#проверка
@then('my drink must have the name "{name}"')
def step_impl(context, name):
    assert context.drink.get_description() == name

@then('my drink must have the price {price:g}')
def step_impl(context, price):
    assert context.drink.get_price() == price
