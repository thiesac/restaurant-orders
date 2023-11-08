from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    # Test 1: Garanta que o nome passado no construtor está correto
    # no atributo name
    pizza = "Pizza"
    pizza = "Pizza"
    dish_pizza = Dish(pizza, 25.00)
    assert dish_pizza.name == pizza

    # Test 2: Garanta que hashs de pratos iguais também sejam iguais
    pasta1 = Dish("Macarronada", 33.50)
    pasta2 = Dish("Macarronada", 33.50)
    assert hash(pasta1) == hash(pasta2)

    # Test 3: Garanta que hashs de pratos diferentes também sejam diferentes
    assert hash(pasta1) != hash(dish_pizza)

    # Test 4: Garanta que o operador de igualdade identifique pratos iguais
    lasagna1 = Dish("Lasanha", 21.00)
    lasagna1.add_ingredient_dependency("queijo mussarela", 200)
    lasagna2 = Dish("Lasanha", 21.00)
    lasagna2.add_ingredient_dependency("queijo mussarela", 200)
    assert lasagna1 == lasagna2

    # Test 5: Garanta que o método __repr__ tenha o comportamento esperado
    expected_repr = "Dish('Lasanha', R$21.00)"
    assert repr(lasagna1) == expected_repr

    # Test 6: Garanta que o método add_ingredient_dependency
    # tenha o comportamento esperado
    lasagna1.add_ingredient_dependency("massa de lasanha", 300)
    assert len(lasagna1.recipe) == 2
    assert lasagna1.recipe.get("queijo mussarela") == 200
    assert lasagna1.recipe.get("massa de lasanha") == 300

    ingredients = lasagna1.get_ingredients()
    assert "massa de lasanha" in ingredients
    assert "queijo mussarela" in ingredients

    # Test 7: Garanta que o método get_restrictions tenha
    # o comportamento esperado
    dish = Dish("Lasanha", 15.0)
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("massa de lasanha")
    dish.add_ingredient_dependency(ingredient1, 200)
    dish.add_ingredient_dependency(ingredient2, 300)
    restrictions = dish.get_restrictions()
    assert any(restriction.name == "LACTOSE" for restriction in restrictions)
    assert any(restriction.name == "GLUTEN" for restriction in restrictions)

    # Test 8: Garanta que o construtor emite ValueError quando deveria
    with pytest.raises(ValueError) as exc_info:
        Dish("Salmão Grelhado", -1)
    assert str(exc_info.value) == "Dish price must be greater then zero."

    # Test 9: Garanta que o construtor emite TypeError quando deveria
    with pytest.raises(TypeError) as exc_info:
        Dish("Lasanha", "52")
    assert str(exc_info.value) == "Dish price must be float."
