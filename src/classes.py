class Product:
    """создание класса Product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.quantity * self.__price + other.quantity * other.price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, prod_list: list):
        name, description, price, quantity = prod_list
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """выводит в консоль значение приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """устанавливает значение приватного атрибута price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input("Цена продукта снижена,уверены, что хотите ее оставить? (y/n)")
            if answer.lower() == "y":
                self.__price = new_price
        else:
            self.__price = new_price


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """создание класса Category"""

    name: str
    description: str
    __products: list

    total_categories = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total = 0
        for i in self.__products:
            total += i.quantity
        return f"{self.name}, количество продуктов: {total} шт."

    def add_product(self, product):
        """добавляет новый продукт в приватный атрибут products"""
        if product is True or product is not None:
            try:
                if isinstance(product, Product) or issubclass(product, Product):
                    self.__products.append(product)
                    Category.product_count += 1
            except Exception as e:
                print(f'Ошибка {e}. Проверьте наследственность добавляемых классов.')

    @property
    def products(self):
        """выводит в консоль значение приватного атрибута products"""
        expected = ""
        for i in self.__products:
            print(f"{str(i)}")
        return expected


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)

product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
category2 = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [product4],
)

product6 = Product("55!!!!!!!!! QLED 4K", "Фоновая подсветка", -2, 1)
product7 = Product("55&&&&&&&&&& QLED 4K", "Фоновая подсветка", 100, 1)
