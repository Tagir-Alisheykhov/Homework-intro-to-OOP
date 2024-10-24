from src.products import Products


class Smartphone(Products):
    """Класс для смартфонов"""

    name: str
    description: str
    price: float | int
    quantity: int | float
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int | float,
        efficiency=None,
        model=None,
        memory=None,
        color=None,
    ):
        """Инициализация основных и дополнительных параметров для модели телефона"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """
        Сложение с условием (Данный класс можно
        складывать объектами только из этого же класса)
        """
        if isinstance(other, self.__class__):
            sum_current_product = self.price * self.quantity
            sum_other_product = other.price * other.quantity
            return sum_current_product + sum_other_product
        else:
            raise TypeError(
                "Объекты класса Smartphone не складываются с другими классами"
            )
