def test_categories_init(first_categories, second_categories):
    """Тест для класса обработки категорий продуктов"""
    assert first_categories.name == "Фрукты"
    assert first_categories.description == "Зарубежные"
    assert len(first_categories.products) == 2

    assert first_categories.category_count == 2
    assert second_categories.category_count == 2

    assert first_categories.product_counts == 6
    assert second_categories.product_counts == 6



