import pytest


def test_lawn_grass(for_lawn_grass):
    """Проверка на корректность инициализации параметров"""
    assert for_lawn_grass.name == "Трава"
    assert for_lawn_grass.description == "Ландшафтный дизайн"
    assert for_lawn_grass.price == 60.0
    assert for_lawn_grass.quantity == 30
    assert for_lawn_grass.country == "Turkey"
    assert for_lawn_grass.germination_period == 10
    assert for_lawn_grass.color == "Green"


def test_lawn_grass_correct_add(for_lawn_grass):
    """Проверка на корректное сложение класса"""
    assert for_lawn_grass + for_lawn_grass == 3600.0


def test_lawn_grass_correct_invalid_addition(for_lawn_grass, for_smartphones):
    """Проверка на возбуждение ошибки при сложении разных классов"""
    with pytest.raises(TypeError):
        assert for_lawn_grass + for_smartphones
