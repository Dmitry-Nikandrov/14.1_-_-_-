from abc import ABC, abstractmethod



class BaseProduct(ABC):

    @abstractmethod
    def __str__(self):
        pass

class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

class Product(BaseProduct, PrintMixin):
    """создание класса Product"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        elif quantity <= 0:
            raise ValueError()
        else:
            self.quantity = quantity
        super().__init__()

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
        'добавляет строковое представление экземпляров класса Category'
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
                print(f"Ошибка {e}. Проверьте наследственность добавляемых классов.")

    def average_price(self):
        "вычисляет среднюю цену товаров в категории"
        try:
            total_sum = sum([i.price for i in self.__products])
            total_quantity = sum([i.quantity for i in self.__products])
            return round(total_sum/total_quantity,2)
        except ZeroDivisionError as e:
            print('В категории отсутствуют товары')
            return 0

    @property
    def products(self):
        """выводит в консоль значение приватного атрибута products"""
        expected = ""
        for i in self.__products:
            print(f"{str(i)}")
        return expected


