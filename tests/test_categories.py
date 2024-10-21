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


def test_categories_str(first_categories):
    """Проверка корректного строкового отображения значений класса"""
    assert str(first_categories) == "Название категории продуктов: 'Фрукты', количество продуктов: 2 шт.\n"


# Для того чтобы значения 'fixture' не увеличились и не обновились,
# тест для класса 'ProductsIterator' будет расположен в данном модуле
def test_products_iterator(products_iterator):
    """Проверки корректности работы класса 'ProductsIterator'"""
    # Переопределяем значение индекса в методе __iter__
    iter(products_iterator)
    assert products_iterator.index == 0

    assert next(products_iterator).name == "Апельсины"
    assert next(products_iterator).name == "Мандарины"
    assert next(products_iterator).name == "Абрикосы"
    assert next(products_iterator).name == "Чернослив"

    with pytest.raises(StopIteration):
        assert next(products_iterator).name

