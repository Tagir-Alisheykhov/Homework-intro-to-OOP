import json
from os import path

from src.categories import Categories
from src.products import Products

data_path = path.join(path.dirname(path.dirname(__file__)), "data/")


def read_json() -> dict:
    """Распаковка json-файла с продуктами и категориями"""
    with open(data_path + "products.json", "r", encoding="UTF-8") as file:
        data_from_js = json.load(file)
    return data_from_js


def create_objects_from_json() -> list:
    """Обработка json-файла с помощью классов и вывод объектов"""
    categories = []
    for category in read_json():
        products = []
        for product in category["products"]:
            products.append(Products(**product))
        category["products"] = products
        categories.append(Categories(**category))
    return categories
