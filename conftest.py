import pytest
from src.classes import Category,Product

@pytest.fixture
def mock_categories():
    return [{"name": "Телевизоры","description": "Современный телевизор","products": [{"name": "55 QLED 4K","description": "Фоновая подсветка","price": 123000, "quantity": 7}]}]

@pytest.fixture
def product5():
    return Product("50 QLED 7K", "Фоновая подсветка", 123000.0, 3)


@pytest.fixture
def product6():
    return Product("50 QLED 54K", "Стерео звук", 200000.0, 20)


@pytest.fixture
def category6(product5, product6):
    return Category(
        "Плазмы",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product5, product6],
    )