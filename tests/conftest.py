import pytest

from src.products import Products
from src.categories import Categories


@pytest.fixture
def first_categories():
    return Categories(
        name="Фрукты",
        description="Зарубежные",
        products=[
            Products("Апельсины", "Из ЮАРа", 60.00, 1000),
            Products("Мандарины", "Из Азербайджана", 40.00, 700)
        ]
    )


@pytest.fixture
def second_categories():
    return Categories(
        name="Фрукты",
        description="Зарубежные",
        products=[
            Products("Апельсины", "Из Африки", 60.00, 1000),
            Products("Мандарины", "Из Азербайджана", 40.00, 700),
            Products("Абрикосы", "Из Узбекистана", 60.00, 1000),
            Products("Чернослив", "Из Молдовы", 120.00, 200)
        ]
    )


@pytest.fixture
def for_products():
    return Products("Виноград", "Из Таджикистана", 50.00, 5000)

