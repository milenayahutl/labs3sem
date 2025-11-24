#TDD стиль: 1. написать проверку чтобы он падал
# 2. написать минимальный код, чтобы тест прошел
# 3. доработать код, не ломая проверки

from beverage import Cappuccino, WhippedCream

def test_Cappuccino():
    capp = Cappuccino()
    assert capp.get_description() == "Cappuccino"
    assert capp.get_price() == 2.0
    print("Cappuccino test passed!")

def test_WhippedCream():
    capp = Cappuccino()
    wc = WhippedCream(capp)
    assert wc.get_description() == "Cappuccino, with whipped cream"
    assert wc.get_price() == 2.5
    print("Whipped cream test passed!")

if __name__ == '__main__':
    test_Cappuccino()
    test_WhippedCream()
    print("All tests passed!")