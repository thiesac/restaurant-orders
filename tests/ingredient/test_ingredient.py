from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Test 1: Garanta que o atributo restrictions seja preenchido corretamente
    cheese = Ingredient("queijo mussarela")
    actual_restrictions_cheese = {str(r) for r in cheese.restrictions}
    cheese_expected_restrictions = {
        str(Restriction.LACTOSE),
        str(Restriction.ANIMAL_DERIVED),
    }
    assert cheese.name == "queijo mussarela"
    assert actual_restrictions_cheese == cheese_expected_restrictions

    # Test 2: Garanta que o método __repr__ tenha o comportamento esperado
    bacon = Ingredient("bacon")
    assert repr(bacon) == "Ingredient('bacon')"

    # Test 3: Garanta que o nome passado no construtor
    # está correto no atributo name
    assert bacon.name == "bacon"

    # Test 4: Garanta que o atributo restrictions seja preenchido corretamente
    bacon_expected_restrictions = {
        str(Restriction.ANIMAL_MEAT),
        str(Restriction.ANIMAL_DERIVED),
    }
    actual_restrictions_bacon = {str(r) for r in bacon.restrictions}
    assert actual_restrictions_bacon == bacon_expected_restrictions

    # Test 5: Garanta que hashs de ingredientes iguais também sejam iguais
    butter1 = Ingredient("manteiga")
    butter2 = Ingredient("manteiga")
    assert hash(butter1) == hash(butter2)

    # Test 6: Garanta que hashs de ingredientes
    # diferentes também sejam diferentes
    assert hash(butter1) != hash(cheese)

    # Test 7: Garanta que o operador de igualdade
    # identifique ingredientes iguais
    salmon1 = Ingredient("salmão")
    salmon2 = Ingredient("salmão")
    assert salmon1 == salmon2
