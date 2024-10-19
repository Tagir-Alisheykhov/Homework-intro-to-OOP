import pytest

from src.categories import Categories
from src.products import Products


@pytest.fixture
def first_categories():
    return Categories(
        name="Фрукты",
        description="Зарубежные",
        products=[
            Products("Апельсины", "Из ЮАРа", 60.00, 1000),
            Products("Мандарины", "Из Азербайджана", 40.00, 700),
        ],
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
            Products("Чернослив", "Из Молдовы", 120.00, 200),
        ],
    )


@pytest.fixture
def for_products():
    return Products("Виноград", "Из Таджикистана", 50.00, 5000)  # Сумма 250000


@pytest.fixture
def for_new_product():
    dict_ = {
        "name": "Banana",
        "description": "Color Yellow",
        "price": 100,
        "quantity": 78,
    }
    return dict_


@pytest.fixture
def for_addition_products():
    return Products("Мандарины", "Из Азербайджана", 40.00, 700)  # Сумма: 28000
