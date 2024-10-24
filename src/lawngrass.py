from src.products import Products


class LawnGrass(Products):
    """Обработка товара 'Трава Зеленая'"""

    name: str
    description: str
    price: float | int
    quantity: int | float
    country: str
    germination_period: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int | float,
        country=None,
        germination_period=None,
        color=None,
    ):
        """Инициализация параметров дочернего продукта"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
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
                "Объекты класса LawnGrass не складываются с другими классами"
            )
