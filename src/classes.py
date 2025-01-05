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


class Category:
    """создание класса Category"""

    name: str
    description: str
    __products: list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def add_product(self, product):
        """добавляет новый продукт в приватный атрибут products"""
        if product is True or product is not None:
            self.__products.append(product)
            Category.total_products += 1

    @property
    def products(self):
        """выводит в консоль значение приватного атрибута products"""
        expected = ""
        for i in self.__products:
            print(f"{i.name}, {i.price} руб. Остаток: {i.quantity}")
        return expected


# if __name__ == "__main__":
product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# print(product1.name)
# print(product1.description)
# print(product1.price)
# print(product1.quantity)
#
# print(product2.name)
# print(product2.description)
# print(product2.price)
# print(product2.quantity)
#
# print(product3.name)
# print(product3.description)
# print(product3.price)
# print(product3.quantity)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2, product3],
)

# print(category1.name == "Смартфоны")
# print(category1.description)
# print(len(category1.products))
# print(category1.total_categories)
# print(category1.total_products)

product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
category2 = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [product4],
)

# print(category2.name)
# print(category2.description)
# print(len(category2.products))
# print(category2.products)
#
# print(Category.total_categories)
# print(Category.total_products)

product6 = Product("55!!!!!!!!! QLED 4K", "Фоновая подсветка", -2, 1)
product7 = Product("55&&&&&&&&&& QLED 4K", "Фоновая подсветка", 100, 1)
