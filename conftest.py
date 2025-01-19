import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def mock_categories():
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор",
            "products": [{"name": "55 QLED 4K", "description": "Фоновая подсветка", "price": 123000, "quantity": 7}],
        }
    ]


@pytest.fixture
def product5():
    return Product("50 QLED 7K", "Фоновая подсветка", 123000.0, 3)


@pytest.fixture
def product6():
    return Product("50 QLED 54K", "Стерео звук", 200000.0, 20)


@pytest.fixture
def category3(product5, product6):
    return Category(
        "Плазмы",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product5, product6],
    )


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_smartphones(smartphone1):
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1])


class BadClass:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


@pytest.fixture
def bad_class():
    return BadClass("new", "new", 100, 15)
