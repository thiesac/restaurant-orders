from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish_name = "Pizza"
    dish = Dish(dish_name, 25.00)
    assert dish.name == dish_name
