from src.models.dish import Dish
from src.models.ingredient import Restriction  # noqa: F401, E261, E501
import pytest


# Req 2
def test_dish():
    pizza = "Pizza"
    dish_pizza = Dish(pizza, 25.00)
    assert dish_pizza.name == pizza

    pasta1 = Dish("Macarronada", 33.50)
    pasta2 = Dish("Macarronada", 33.50)
    assert hash(pasta1) == hash(pasta2)
    assert hash(pasta1) != hash(dish_pizza)

    lasagna1 = Dish("Lasanha", 21.00)
    lasagna1.add_ingredient_dependency("queijo mussarela", 200)
    lasagna2 = Dish("Lasanha", 21.00)
    lasagna2.add_ingredient_dependency("queijo mussarela", 200)
    assert lasagna1 == lasagna2

    expected_repr = "Dish('Lasanha', R$21.00)"
    assert repr(lasagna1) == expected_repr

    lasagna1.add_ingredient_dependency("massa de lasanha", 300)
    assert len(lasagna1.recipe) == 2
    assert lasagna1.recipe.get("queijo mussarela") == 200
    assert lasagna1.recipe.get("massa de lasanha") == 300

    ingredients = lasagna1.get_ingredients()
    assert "massa de lasanha" in ingredients
    assert "queijo mussarela" in ingredients

    with pytest.raises(ValueError) as exc_info:
        Dish("Salmão Grelhado", -1)
    assert str(exc_info.value) == "Dish price must be greater then zero."

    with pytest.raises(TypeError) as exc_info:
        Dish("Lasanha", "52")
    assert str(exc_info.value) == "Dish price must be float."
