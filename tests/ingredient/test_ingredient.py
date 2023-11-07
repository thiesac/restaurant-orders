from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese = Ingredient("queijo mussarela")
    # the str() function is used to convert the enum elements to strings
    cheese_expected_restrictions = {
        str(Restriction.LACTOSE),
        str(Restriction.ANIMAL_DERIVED),
    }
    actual_restrictions_cheese = {str(r) for r in cheese.restrictions}
    assert cheese.name == "queijo mussarela"
    assert actual_restrictions_cheese == cheese_expected_restrictions

    bacon = Ingredient("bacon")
    assert repr(bacon) == "Ingredient('bacon')"
    bacon_expected_restrictions = {
        str(Restriction.ANIMAL_MEAT),
        str(Restriction.ANIMAL_DERIVED),
    }
    actual_restrictions_bacon = {str(r) for r in bacon.restrictions}
    assert bacon.name == "bacon"
    assert actual_restrictions_bacon == bacon_expected_restrictions

    butter1 = Ingredient("manteiga")
    butter2 = Ingredient("manteiga")
    assert hash(butter1) == hash(butter2)
    assert hash(butter1) != hash(cheese)

    salmon1 = Ingredient("salmão")
    salmon2 = Ingredient("salmão")
    assert salmon1 == salmon2
