class ProductsIterator:
    """Класс для обработки категории продуктов"""

    def __init__(self, categories_obj):
        self.categories = categories_obj
        self.start_index = 0

    def __iter__(self):
        # Для того чтобы значение каждый раз обновлялось
        self.start_index = 0
        return self

    def __next__(self):
        if self.start_index < len(self.categories.products_list):
            category = self.categories.products_list[self.start_index]
            self.start_index += 1
            return category
        else:
            raise StopIteration


# P.S. ПОСМОТРИ ПРАКТИКУ СОЗДАНИЯ ИТЕРИРУЕМЫХ ОБЪЕКТОВ И ПРИМЕНИ ЗДЕСЬ
