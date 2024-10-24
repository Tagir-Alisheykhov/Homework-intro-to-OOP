from typing import Any

from src.products import Products


class Categories:
    """Класс для обработки категорий продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_counts = 0

    def __init__(self, name, description, products):
        """Инициализация категорий продуктов"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Categories.category_count += 1
        Categories.product_counts += len(products) if products else 0

    def __str__(self) -> Any:
        """Строковое отображение названия категории товаров, и их количества"""
        total_number_of_prods = 0
        for product in self.__products:
            total_number_of_prods += product.quantity
        return (
            f"Название категории продуктов: '{self.name}'. "
            f"Количество продуктов: {total_number_of_prods} шт.\n"
        )

    def add_product(self, product: Products) -> None:
        """Добавление нового товара (объект класса) в список товаров"""
        if isinstance(product, Products):
            self.__products.append(product)
            Categories.product_counts += 1
        else:
            raise TypeError("Неправильный тип данных")

    @property
    def products_list(self) -> Any:
        """Вызов списка продуктов"""
        return self.__products

    @property
    def products(self) -> Any:
        """"""
        products_str = ""
        for product in self.__products:
            products_str += str(product)
        return products_str
