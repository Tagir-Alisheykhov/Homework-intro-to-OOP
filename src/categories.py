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

    def add_product(self, product):
        """Добавление нового товара (объект класса) в список товаров"""
        self.__products.append(product)
        Categories.product_counts += 1

    @property
    def products_for_test(self):
        """Возврат списка продуктов"""
        return self.__products

    @property
    def products(self):
        """"""
        products_str = ""
        for product in self.__products:
            products_str += (f"{product.name}, "
                             f"{product.price} руб. "
                             f"Остаток: {product.quantity} шт\n")
        return products_str


