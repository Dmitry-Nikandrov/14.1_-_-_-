from unittest.mock import patch

import pytest

from src.classes import Category, Product


def test_product_init(product5):
    assert product5.name == "50 QLED 7K"
    assert product5.description == "Фоновая подсветка"
    assert product5.quantity == 3
    with pytest.raises(ValueError):
        Product("Samsung ", "256 камера", 180000.0, quantity=-5)
    with pytest.raises(ValueError):
        Product("Samsung ", "256 камера", 180000.0, quantity=0)


def test_categories_init(category3):
    assert category3.name == "Плазмы"
    assert (
        category3.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


def test_categories_count(category3, category1, category2):
    assert Category.total_categories == 4
    assert len(category1.products) == 0
    assert len(category2.products) == 0
    assert len(category3.products) == 0


def test_product_1(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5


def test_product_2(product2):
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.quantity == 8


def test_classmethod_new_product():
    example_Product = Product.new_product(["new_name", "new_description", "new_price", 10])
    assert example_Product.name == "new_name"
    assert example_Product.description == "new_description"
    assert example_Product.quantity == 10


def test_property_price_1(product6):
    assert product6.price == 200000.0


def test_property_price_2(product5):
    assert product5.price == 123000.0


def test_add_product(capsys, category1):
    example_Product = Product.new_product(["new_name", "new_description", "new_price", 10])
    category1.add_product(example_Product)
    category1.products
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, "
        "5)\n"
        "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"
        "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)\n"
        "Product(new_name, new_description, new_price, 10)\n"
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "new_name, new_price руб. Остаток: 10 шт."
    )


def test_property_products(capsys, category3):
    category3.products
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(50 QLED 7K, Фоновая подсветка, 123000.0, 3)\n"
        "Product(50 QLED 54K, Стерео звук, 200000.0, 20)\n"
        "50 QLED 7K, 123000.0 руб. Остаток: 3 шт.\n"
        "50 QLED 54K, 200000.0 руб. Остаток: 20 шт."
    )


def test_property_price(product5):
    assert product5.price == 123000


def test_price_setter_1(product5):
    product5.price = 150000
    assert product5.price == 150000


def test_price_setter_2(product5):
    product5.price = 0
    assert product5.price == 123000


def test_price_setter_3(capsys, product5):
    product5.price = -100000
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(50 QLED 7K, Фоновая подсветка, 123000.0, 3)\n" "Цена не должна быть нулевая или отрицательная"
    )


@patch("builtins.input", return_value="Y")
def test_price_setter_4(capsys, product5):
    product5.price = 80000
    assert product5.price == 80000


@patch("builtins.input", return_value="n")
def test_price_setter_5(capsys, product5):
    product5.price = 80000
    assert product5.price == 123000


def test_average_price(category3,product5,product6):
    assert category3.average_price() == 14043.48
    assert Category(
        "Плазмы",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        []).average_price() == 0