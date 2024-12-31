import json
import os
from src.classes import Category, Product


def load_json_data(path: str) -> list:
    """вовзращает python-объект из файла json"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_classes_from_json(data: list) -> list:
    """возвращает список словарей по экземплярам класса Product и Category из списка словарей"""
    try:
        categories_list = []
        for category in data:
            prod_list = []
            for product in category["products"]:
                prod_list.append(
                    Product(
                        product["name"],
                        product["description"],
                        product["quantity"],
                        product["price"],
                    )
                )
            category["products"] = prod_list
            categories_list.append(Category(category["name"], category["description"], category["products"]))
        return categories_list
    except Exception:
        return []
