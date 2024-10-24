from src.categories import Categories
from src.products import Products
from src.utils import create_objects_from_json
from src.products_iterator import ProductsIterator
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def main() -> list:
    """Объединяет в себе весь функционал программы"""
    return create_objects_from_json()


if __name__ == "__main__":

    # categories = main()
    # for category in categories:
    #     obj_category_iterator = ProductsIterator(category)
    #     # Выводит общее количество продуктов в каждой категории
    #     print(category)

        # Отображение итератора
        # for i in obj_category_iterator:
        #     print(i)
        #     print()

    #     print()
    #     print(category.name)
    #     print(category.description)
    #     print(category.products)
    #     print(category)  # Выводит строковое отображение категории


    # # --------------------------------------------------
    # # Проверки для класса Products
    # # -------------------------------------------------
    #
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
    # print()
    # print(prod_1)  # Banana, 99.99 руб. Остаток: 20 шт.
    # print(prod_2)  # Banana, 110.0 руб. Остаток: 98 шт.
    #
    # test_product = Products("Avocado", "Color Green", 10000.00, 1)
    # sum_products = prod_1 + test_product
    # print(f"This is sum products {sum_products}")  # This is sum products 11999.8


    # # --------------------------------------------------
    # # Проверки для класса Categories
    # # --------------------------------------------------
    # print("НОВЫЙ ВЫЗОВ")
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
    # # # -------------------------
    # #
    # obj_category.add_product(1)
    # # # -------------------------
    # #
    # print(obj_category.products)
    # # # -------------------------
    # #
    # # print(obj_category.product_counts)
    # # print(obj_category.category_count)
    # #
    # # print(obj_category.products_list)
    # #
    # # print(obj_category.products)
    # banana, 79.9 руб. Остаток: 10 шт.
    # mandarin, 69.8 руб. Остаток: 20 шт.
    # mandarin, 49.9 руб. Остаток: 10 шт.
    # granate, 100.99 руб. Остаток: 40 шт.
    # Kivi, 80.99 руб. Остаток: 50 шт.
    #
    # print(obj_category)

    # ---- Отдельная проверка для Categories ----

    # smartphone = Smartphone("Samsung", "Современный дизайн", 90000.0, 1,
    #                         "2-х ядерный процессор", "Galaxy C23 Ultra", 256, "Серый")
    # lawn_grass = LawnGrass("Трава", "Ландшафтный дизайн", 60.0, 30,
    #                       "Turkey", 10, "Green")






    # -----------------------------------------------------------------
    # ПРОВЕРКИ ДЛЯ КЛАССА ИТЕРАТОРА (Вспомогательного)
    # -----------------------------------------------------------------
    # Создайте новый вспомогательный класс, с помощью которого можно перебирать
    # товары одной категории, например в цикле for. Для этого новый класс должен
    # принимать на вход объект класса категории и производить итерацию по товарам,
    # которые хранятся в данной категории. То есть метод выполнения следующего шага
    # итерации должен возвращать очередной товар категории.

    # т.е. мы принимаем объект класса Categories, после этого
    # products_and_categories = Categories()
    # т.е. для каждой категории берем отдельно

    # obj_category_ = Categories()
    # #
    # product1 = Products("banana", "Afrika", 79.90, 10)
    # product2 = Products("mandarin", "Nepal", 69.80, 20)
    # product3 = Products("mandarin", "India", 49.90, 10)
    # product4 = Products("granate", "Russia", 100.99, 40)
    # # # # -------------------------
    # #
    # obj_categories_ = Categories("Fruit", "Vkusniye", [product1, product2, product3, product4])
    #
    # obj_category_iterator = ProductsIterator(obj_categories_)
    #
    # for i in obj_category_iterator:
    #     print(i)
    #     print(type(i))
    # # # -------------------------


    # # -----------------------------------------------------------------
    # # ПРОВЕРКИ ДЛЯ КЛАССОВ 'LawnGrass' и 'Smartphone'
    # # -----------------------------------------------------------------
    #
    # smartphone = Smartphone("Samsung", "Современный дизайн", 90000.0, 1,
    #                         "2-х ядерный процессор", "Galaxy C23 Ultra", 256, "Серый")
    # lawn_grass = LawnGrass("Трава", "Ландшафтный дизайн", 60.0, 30,
    #                       "Turkey", 10, "Green")

    # Проверка на то, что однотипные продукты складываются успешно
    # print(smartphone + smartphone)  # 180000.0
    # print(lawn_grass + lawn_grass)  # 3600.0

    # print(lawn_grass + 1)  # raise TypeError

    # Проверка на то, что не однотипные продукты вызывают ошибку при сложении
    # print(lawn_grass + smartphone)  # TypeError
