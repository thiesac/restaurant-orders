from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    pizza = "Pizza"
    dish_pizza = Dish(pizza, 25.00)
    assert dish_pizza.name == pizza

    pasta1 = Dish("Macarronada", 33.50)
    pasta2 = Dish("Macarronada", 33.50)
    assert hash(pasta1) == hash(pasta2)

    with pytest.raises(ValueError) as exc_info:
        Dish("Salmão Grelhado", -1)
    assert str(exc_info.value) == "Dish price must be greater then zero."

    with pytest.raises(TypeError) as exc_info:
        Dish("Lasanha", "52")
    assert str(exc_info.value) == "Dish price must be float."
