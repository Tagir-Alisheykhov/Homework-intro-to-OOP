def test_products_init(for_products):
    """Тест для класса обработки продуктов"""
    assert for_products.name == "Виноград"
    assert for_products.description == "Из Таджикистана"
    assert for_products.price == 50.00
    assert for_products.quantity == 5000

