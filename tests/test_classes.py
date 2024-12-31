from src.classes import Category, category1, category2, product1, product2


def test_product_init(product5):
    assert product5.name == "50 QLED 7K"
    assert product5.description == "Фоновая подсветка"
    assert product5.quantity == 3


def test_categories_init(category3):
    assert category3.name == "Плазмы"
    assert (
        category3.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


def test_categories_count(category3):
    assert Category.total_categories == 4
    assert len(category1.products) == 3
    assert len(category2.products) == 1
    assert len(category3.products) == 2


def test_product_1():
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5


def test_product_2():
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.quantity == 8
