'''Шаблон: Строитель'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Cook(ABC):
    @property
    @abstractmethod
    def salad(self) -> None:
        pass
    @abstractmethod
    def add_vegetables(self) -> None:
        pass
    @abstractmethod
    def add_meat(self) -> None:
        pass
    @abstractmethod
    def add_sauce(self) -> None:
        pass

class SaladCook(Cook):
    def __init__(self) -> None:
        self.reset()
    def reset(self) -> None:
        self._salad = CookedSalad()
    @property
    def salad(self) -> CookedSalad:
        salad = self._salad
        self.reset()
        return salad
    def add_vegetables(self) -> None:
        self._salad.add("vegetables")
    def add_meat(self) -> None:
        self._salad.add("meat")
    def add_sauce(self) -> None:
        self._salad.add("sauce")

class CookedSalad():
    def __init__(self) -> None:
        self.ingredients = []
    def add(self, ingredient: Any) -> None:
        self.ingredients.append(ingredient)
    def list_ingredients(self) -> None:
        print(f"Salad ingredients: {', '.join(self.ingredients)}", end="")

class Chief:
    def __init__(self) -> None:
        self._cook = None
    @property
    def cook(self) -> Cook:
        return self._cook
    @cook.setter
    def cook(self, cook: Cook) -> None:
        self._cook = cook
    def cook_meat_salad(self) -> None:
        self.cook.add_vegetables()
        self.cook.add_meat()
        self.cook.add_sauce()
    def cook_vegetarian_salad(self) -> None:
        self.cook.add_vegetables()
        self.cook.add_sauce()

if __name__ == "__main__":
    chief = Chief()
    cook = SaladCook()
    chief.cook = cook
    print("Cooking meat salad: ")
    chief.cook_meat_salad()
    cook.salad.list_ingredients()
    print("Cooking vegetarian salad: ")
    chief.cook_vegetarian_salad()
    cook.salad.list_ingredients()

