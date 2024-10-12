class Products:
    """Класс для обработки параметров продукта"""

    name: str
    description: str
    price: float | int
    quantity: int | float
    price_test = 20.5

    def __init__(self, name, description, price=0.0, quantity=0):
        """Инициализация параметров продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product: dict, list_products: list) -> object:
        """
        Создание нового продукта и слияние количества наименования
        того же товара из принимаемого списка продуктов.
        А также сравнение цен и установка цены в пользу большей
        """
        new_prod = cls(**dict_product)
        for product in list_products:
            product_from_list = cls(**product)
            if product_from_list.name == new_prod.name:
                count_products = new_prod.quantity + product_from_list.quantity
                product_from_list.quantity = count_products
                new_prod.quantity = count_products
                max_price = max(new_prod.__price, product_from_list.__price)
                product_from_list.__price, new_prod.__price = max_price, max_price
        return new_prod

    @property
    def price(self):
        """Для вывода цены продукта"""
        return float(self.__price)

    @price.setter
    def price(self, new_price: int | float):
        """
        Дополнительные проверки для корректного ввода цены товара пользователем
        """
        if new_price <= 0:
            print("\nЦена не должна быть нулевая или отрицательная\n")
        else:
            # Заметка: self.__price - это уже имеющаяся цена для обрабатываемого продукта
            if new_price < self.__price:
                choice_y_n = (
                    input("Вы действительного хотите снизить цену?\nY/N\n").lower())
                if choice_y_n == "y".strip():
                    self.__price = new_price
            else:
                self.__price = new_price
