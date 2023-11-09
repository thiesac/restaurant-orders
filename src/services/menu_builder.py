from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
# from models.ingredient import Restriction

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        if restriction is None:
            return [
                {
                    "dish_name": dish.name,
                    "ingredients": [
                        {"name": ingredient.name, "quantity": quantity}
                        for ingredient, quantity in dish.recipe.items()
                    ],
                    "price": dish.price,
                    "restrictions": [str(r) for r in dish.get_restrictions()],
                }
                for dish in self.menu_data.dishes
            ]
        else:
            filtered_dishes = [
                {
                    "dish_name": dish.name,
                    "ingredients": [
                        {"name": ingredient.name, "quantity": quantity}
                        for ingredient, quantity in dish.recipe.items()
                    ],
                    "price": dish.price,
                    "restrictions": [str(r) for r in dish.get_restrictions()],
                }
                for dish in self.menu_data.dishes
                if restriction not in dish.get_restrictions()
            ]
            return filtered_dishes


# menu_builder = MenuBuilder()
# # menu_builder.make_order("lasanha presunto")
# print(menu_builder)
# print(menu_builder.menu_data.dishes)
# menu_builder.get_main_menu(restriction=Restriction.ANIMAL_MEAT)

# # python3 -m src.services.menu_builder
