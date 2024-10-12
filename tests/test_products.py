from src.products import Products


def test_products_init(for_products):
    """Тест для класса обработки продуктов"""
    assert for_products.name == "Виноград"
    assert for_products.description == "Из Таджикистана"
    assert for_products.price == 50.00
    assert for_products.quantity == 5000


def test_products_create():
    """Проверка корректности инициализации классом параметров товара"""
    product = Products("Banana", "Color Yellow", 99.99, 20)
    assert product.name == "Banana"
    assert product.description == "Color Yellow"
    assert product.price == 99.99
    assert product.quantity == 20


def test_products_invalid_price_update(capsys, for_products):
    """Перехват потока вывода сообщения в из getter"""
    # Заметка: Важно прописывать объект класса (for_products.price)
    for_products.price = 0
    # Определяем capsys
    message = capsys.readouterr()
    # Проверка сообщения из потока выводов с удалением лишних символов
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
