class Products:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price=0.0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# print(Products)

# object1 = Products("Апельсины", "Из Африки", 60.00, 1000)
#
#
# if __name__ == "__main__":
#     print(object1.name)
#     print(object1.description)
#     print(object1.price)
#     print(object1.quantity)
