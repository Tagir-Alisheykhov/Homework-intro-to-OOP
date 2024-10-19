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

    def __str__(self):
        """Строковое отображение названия категории товаров, и их количества"""
        return (f"Название категории продуктов: '{self.name}', "
                f"количество продуктов: {len(self.__products)} шт.\n")

    def __add__(self, other):
        """Суммирование товаров"""
        for product in self.__products:
            print(f'\nproduct name {product.name}, price {product.price}\n' +
                  f'other name {product.name}, price {product.price}\n')

    def add_product(self, product: Products):
        """Добавление нового товара (объект класса) в список товаров"""
        self.__products.append(product)
        Categories.product_counts += 1

    @property
    def products_list(self):
        """Возврат списка продуктов"""
        return self.__products

    @property
    def products(self) -> str:
        """"""
        products_str = ""
        for product in self.__products:
            products_str += str(product)
        return products_str
