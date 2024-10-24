from src.products import Products


class LawnGrass(Products):
    """ Обработка товара 'Трава Зеленая' """
    name: str
    description: str
    price: float | int
    quantity: int | float
    country: str
    germination_period: int
    color: str

    def __init__(self, name: str, description: str, price: float | int, quantity: int | float,
                 country: str = None, germination_period: int = None, color: str = None):
        """ Инициализация параметров дочернего продукта """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """ Сложение с условием """
        if other is self:
            sum_current_product = self.price * self.quantity
            sum_other_product = other.price * other.quantity
            return sum_current_product + sum_other_product
        else:
            raise TypeError("Объекты класса LawnGrass не складываются с другими классами")

# res = LawnGrass("Samsung", "Современный дизайн",90000, 1, "Russia", 10, "Green")
#
# print(res.name)
# print(res.description)
# print(res.price)
# print(res.quantity)
# print(res.country)
# print(res.germination_period)
# print(res.color)