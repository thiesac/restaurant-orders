from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    pizza = "Pizza"
    dish_pizza = Dish(pizza, 25.00)
    assert dish_pizza.name == pizza

    with pytest.raises(ValueError) as exc_info:
        Dish("Salmão Grelhado", -1)
    assert str(exc_info.value) == "Dish price must be greater then zero."
