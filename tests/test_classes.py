from src.classes import Category, product1,product2,product3,product4


def test_product_init(product5):
    assert product5.name == "50 QLED 7K"
    assert product5.description == "Фоновая подсветка"
    assert product5.quantity == 3

def test_categories_init(category6):
    assert category6.name == "Плазмы"
    assert (
        category6.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

def test_categories_count():
    assert Category.total_categories == 3
    assert Category.total_products == 6

def test_product_1():
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.quantity == 5

def test_product_2():
    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.quantity == 8
