import pytest

from src.classes_iterator import ProductIterator


def test_str_prod(capsys, product5):
    print(str(product5))
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(50 QLED 7K, Фоновая подсветка, 123000.0, 3)\n" "50 QLED 7K, 123000.0 руб. Остаток: 3 шт."
    )


def test_add_prod(product5, product6):
    assert product5 + product6 == 4369000


def test_str_cat(capsys, category3):
    print(str(category3))
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(50 QLED 7K, Фоновая подсветка, 123000.0, 3)\n"
        "Product(50 QLED 54K, Стерео звук, 200000.0, 20)\n"
        "Плазмы, количество продуктов: 23 шт."
    )


def test_iterator_1(category1):
    assert ProductIterator(category1).index == 0
    with pytest.raises(StopIteration):
        next(ProductIterator(category1))


def test_iterator_2(capsys, category1):
    for i in ProductIterator(category1):
        print(i)
    message = capsys.readouterr()
    assert message.out.strip() == (
        "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, "
        "5)\n"
        "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"
        "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)\n"
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
