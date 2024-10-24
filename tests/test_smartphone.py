import pytest


def test_lawn_grass(for_smartphones):
    """Проверка на корректность инициализации параметров"""
    assert for_smartphones.name == "Samsung"
    assert for_smartphones.description == "Современный дизайн"
    assert for_smartphones.price == 90000.0
    assert for_smartphones.quantity == 1
    assert for_smartphones.efficiency == "2-х ядерный процессор"
    assert for_smartphones.model == "Galaxy C23 Ultra"
    assert for_smartphones.memory == 256
    assert for_smartphones.color == "Серый"


def test_lawn_grass_correct_add(for_smartphones):
    """Проверка на корректное сложение класса"""
    assert for_smartphones + for_smartphones == 180000.0


def test_lawn_grass_correct_invalid_addition(for_lawn_grass, for_smartphones):
    """Проверка на возбуждение ошибки при сложении разных классов"""
    with pytest.raises(TypeError):
        assert for_smartphones + for_lawn_grass
