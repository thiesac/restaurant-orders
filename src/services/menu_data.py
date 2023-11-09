import csv
from typing import Dict, Set

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    # Initialize the class with the source path for the CSV file
    def __init__(self, source_path: str) -> None:
        # Set the source path to the provided path
        self.source_path = source_path
        # Initialize an empty set to store the dishes
        self.dishes: Set[Dish] = set()
        # Call the private method to read the CSV file
        self._read_csv()

    # Private method to read the CSV file
    def _read_csv(self) -> None:
        with open(self.source_path, newline="") as csvfile:
            # Use csv.DictReader to read the rows as dictionaries
            reader = csv.DictReader(csvfile)
            # Create a dictionary to map dish names to Dish instances
            dishes_map: Dict[str, Dish] = {}

            for row in reader:
                dish_name, price = self._extract_dish_info(row, dishes_map)
                ingredient, recipe_amount = self._extract_ingredient_info(row)

                if dish_name not in dishes_map:
                    # If dish not in dishes_map, create a new Dish instance
                    # and add it to dishes_map and self.dishes
                    dish = Dish(dish_name, price)
                    dishes_map[dish_name] = dish
                    self.dishes.add(dish)
                else:
                    # If the dish is already in dishes_map, get
                    # the corresponding Dish instance
                    dish = dishes_map[dish_name]

                # Create an Ingredient instance with the extracted
                # ingredient name
                ingredient = Ingredient(ingredient)
                # Add the ingredient and recipe amount to the dish's recipe
                dish.add_ingredient_dependency(ingredient, recipe_amount)

    # Private method to extract dish information from a row
    def _extract_dish_info(
        self, row: Dict, dishes_map: Dict[str, Dish]
    ) -> tuple:
        dish_name = row["dish"]
        price = float(row["price"])
        return dish_name, price

    # Private method to extract ingredient information from a row
    def _extract_ingredient_info(self, row: Dict) -> tuple:
        ingredient_name = row["ingredient"]
        recipe_amount = float(row["recipe_amount"])
        return ingredient_name, recipe_amount


# menu_data = MenuData("tests/mocks/menu_base_data.csv")
# print(menu_data.dishes)
