from src.products import Products


class Smartphone(Products):
    """ Подкласс для смартфонов """
    name: str
    description: str
    price: float | int
    quantity: int | float
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(self, name: str, description: str, price: float | int, quantity: int | float,
                 efficiency: str = None, model: str = None, memory: int = None, color: str = None):
        """ Инициализация основных и дополнительных параметров для модели телефона """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """ Сложение с условием """
        if other is self:
            sum_current_product = self.price * self.quantity
            sum_other_product = other.price * other.quantity
            return sum_current_product + sum_other_product
        else:
            raise TypeError("Объекты класса Smartphone не складываются с другими классами")






# res = Smartphone("Samsung", "Современный дизайн",90000, 1, "2-х ядернвй процессор", "Galaxy C23 Ultra", "256", "Серый")
#
# print(res.name)
# print(res.description)
# print(res.price)
# print(res.quantity)
# print(res.efficiency)
# print(res.model)
# print(res.memory)
# print(res.color)


