from src.products import Products


class Categories:
    name: str
    description: str
    products: list
    category_count = 0  # Список объектов класса Product
    product_counts = 0  #

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products if products else []
        Categories.category_count += 1
        Categories.product_counts += len(products) if products else 0


if __name__ == "__main__":
    products1 = Products("Апельсины", "Из Африки", 60.00, 1000)
    products2 = Products("Мандарины", "Из Азербайджана", 40.00, 700)

    categories = Categories("Фрукты", "Марокканские", [products1, products2])

    print(categories.name)
    print(categories.description)
    print(categories.products)

    print(categories.category_count)
    print(Categories.product_counts)
