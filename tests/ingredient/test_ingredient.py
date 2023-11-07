from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese = Ingredient("queijo mussarela")
    # the str() function is used to convert the enum elements to strings
    expected_restrictions = {
        str(Restriction.LACTOSE),
        str(Restriction.ANIMAL_DERIVED),
    }
    actual_restrictions = {str(r) for r in cheese.restrictions}
    assert cheese.name == "queijo mussarela"
    assert actual_restrictions == expected_restrictions
