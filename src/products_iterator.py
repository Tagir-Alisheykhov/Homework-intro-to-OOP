class ProductsIterator:
    """Класс для обработки категории продуктов"""

    def __init__(self, categories_obj):
        """
        Инициализация объекта категории
        продуктов и начального индекса
        """
        self.categories = categories_obj
        self.index = 0

    def __iter__(self):
        """Создание итератора с обновляющимся начальным индексом"""
        # Для того чтобы значение каждый раз обновлялось
        self.index = 0
        return self

    def __next__(self):
        """Перебор итератора с добавлением условий"""
        if self.index < len(self.categories.products_list):
            category = self.categories.products_list[self.index]
            self.index += 1
            return category
        else:
            raise StopIteration
