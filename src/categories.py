class Categories:
    """Класс для обработки категорий продуктов"""

    name: str
    description: str
    products: list
    category_count = 0  # Список объектов класса Product
    product_counts = 0  #

    def __init__(self, name, description, products):
        """Инициализация категорий продуктов"""
        self.name = name
        self.description = description
        self.products = products if products else []
        Categories.category_count += 1
        Categories.product_counts += len(products) if products else 0
