from src.utils import create_objects_from_json

from src.products import Products
from src.categories import Categories


def main() -> list:
    """Объединяет в себе весь функционал программы"""
    return create_objects_from_json()


if __name__ == "__main__":
    products = main()
    for product in products:
        print()
        print(product.name)
        print(product.description)
        print(product.products)

    # Проверки для класса Products
    # # Инициализация и проверка первого продукта
    # prod_1 = Products("Banana", "Color Yellow", 99.99, 20)
    # print(prod_1.name)
    # print(prod_1.description)
    # print(prod_1.price)
    # print(prod_1.quantity)
    #
    # dict_ = {
    #     'name': 'Banana',
    #     'description': 'Color Yellow',
    #     'price': 100,
    #     'quantity': 78
    # }
    # list_ = [
    #     {"name": "Banana", "description": "America", "price": 100.00, "quantity": 20},
    #     {"name": "mandarin", "description": "Nepal", "price": 69.80, "quantity": 20},
    #     {"name": "granate", "description": "Russia", "price": 100.99, "quantity": 40}
    # ]
    #
    # prod_2 = Products.new_product(dict_, list_)  # Инициализация и проверка второго продукта через метод .new_product
    # print(prod_2.name)
    # print(prod_2.description)
    # print(prod_2.price)
    # print(prod_2.quantity)
    #
    # prod_2.price = 110  # Снижение цены для prod_2
    # print(prod_2.price)
    #
    #
    #
    # # Проверки для класса Categories
    # # -------------------------
    #
    # product1 = Products("banana", "Afrika", 79.90, 10)
    # product2 = Products("mandarin", "Nepal", 69.80, 20)
    # product3 = Products("mandarin", "India", 49.90, 10)
    # product4 = Products("granate", "Russia", 100.99, 40)
    # # # -------------------------
    #
    # obj_category = Categories("Fruit", "Vkusniye", [product1, product2, product3, product4])
    # print(obj_category.products)
    # print(obj_category.product_counts)
    # print(obj_category.category_count)
    # # -------------------------
    #
    # product5 = Products("Kivi", "green", 80.99, 50)
    # # -------------------------
    #
    # obj_category.add_product(product5)
    # # -------------------------
    #
    # print(obj_category.products)
    # # -------------------------
    #
    # print(obj_category.product_counts)
    # print(obj_category.category_count)
    #
    # print(obj_category.products_for_test)
