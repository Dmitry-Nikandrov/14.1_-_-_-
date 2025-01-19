import pytest

from src.classes import category1
from src.classes_iterator import ProductIterator


def test_str_prod(capsys, product5):
    print(str(product5))
    message = capsys.readouterr()
    assert message.out.strip() == "50 QLED 7K, 123000.0 руб. Остаток: 3 шт."


def test_add_prod(product5, product6):
    assert product5 + product6 == 4369000


def test_str_cat(capsys, category3):
    print(str(category3))
    message = capsys.readouterr()
    assert message.out.strip() == "Плазмы, количество продуктов: 23 шт."


def test_iterator_1():
    assert ProductIterator(category1).index == 0
    with pytest.raises(StopIteration):
        next(ProductIterator(category1))


def test_iterator_2(capsys):
    for i in ProductIterator(category1):
        print(i)
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
