class Products:
    """Класс для обработки продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price=0.0, quantity=0):
        """Инициализация продуктов"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
