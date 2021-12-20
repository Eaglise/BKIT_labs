'''Шаблон: Мост + Строитель'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# Абстрактный класс
class Chief:
    def __init__(self, cook: Cook) -> None:
        self.cook = cook
    def StartCooking(self) -> str:
        return ('Started cooking!')

class SaladChief(Chief):
    def cook_meat_salad(self) -> str:
        self.cook.add_vegetables()
        self.cook.add_meat()
        self.cook.add_sauce()
        return "Cooking meat salad..."
    def cook_vegetarian_salad(self) -> None:
        self.cook.add_vegetables()
        self.cook.add_sauce()
        return "Cooking vegetarian salad..."

#Реализация
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
    def list_ingredients(self) -> str:
        if not self.ingredients:
            return "There is no salad ready"
        else:
            return f"Salad ingredients: {', '.join(self.ingredients)}"

if __name__ == "__main__":
    cook = SaladCook()
    chief = SaladChief(cook)
    print(cook.salad.list_ingredients())
    cooking = chief.cook_meat_salad()
    print(cooking)
    meal = cook.salad.list_ingredients()
    print(meal)