import pytest


def test_add_products(smartphone1, smartphone2, grass1):
    assert smartphone1 + smartphone2 == 2580000
    with pytest.raises(TypeError):
        assert smartphone1 + grass1


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_str_category(category_smartphones):
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 5 шт."


def test_add_product(capsys, category_smartphones, smartphone2, bad_class):
    category_smartphones.add_product(smartphone2)
    category_smartphones.products
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, "
        "180000.0, 5)\n"
        "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )
    category_smartphones.add_product(bad_class)
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Ошибка issubclass() arg 1 must be a class. Проверьте наследственность " "добавляемых классов."
    )
