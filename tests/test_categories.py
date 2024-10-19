import pytest


def test_categories_init(first_categories, second_categories):
    """Тест для класса обработки категорий продуктов"""
    #
    assert first_categories.name == "Фрукты"
    #
    assert first_categories.description == "Зарубежные"
    assert len(first_categories.products_list) == 2

    assert first_categories.category_count == 2
    assert second_categories.category_count == 2

    assert first_categories.product_counts == 6
    assert second_categories.product_counts == 6


def test_categories_products_property(first_categories):
    """
    Проверка корректности работы getter класса и вывода ожидаемого результата
    :param first_categories: Список товаров из /conftest.py
    """
    assert (
        first_categories.products
        == "Апельсины, 60.0 руб. Остаток: 1000 шт.\nМандарины, 40.0 руб. Остаток: 700 шт.\n"
    )


def test_categories_products_setter(first_categories, for_products):
    """Проверка корректности работы метода класса и вывода ожидаемого результата"""
    assert len(first_categories.products_list) == 2
    first_categories.add_product(for_products)
    assert len(first_categories.products_list) == 3

