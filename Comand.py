'''Шаблон: Команда+ Мост + Строитель'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Order(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class SaladOrder(Order):
    def __init__(self, reciever: SaladChief, orderText: str) -> None:
        self._reciever = reciever
        self._orderText = orderText
    def execute(self) -> None:
        print("*Order is passed to the Chief*")
        self._reciever.start_cooking(self._orderText)

# Абстрактный класс
class Chief:
    def __init__(self, cook: Cook) -> None:
        self.cook = cook

class SaladChief(Chief):
    def cook_meat_salad(self) -> None:
        self.cook.add_vegetables()
        self.cook.add_meat()
        self.cook.add_sauce()
        print("*The meat salad is ready*")
    def cook_vegetarian_salad(self) -> None:
        self.cook.add_vegetables()
        self.cook.add_sauce()
        print("*The vegetable salad is ready*")
    def start_cooking(self, orderText: str) -> None:
        if orderText == "meat salad":
            self.cook_meat_salad()
        elif orderText == "vegetarian salad":
            self.cook_vegetarian_salad()
        else:
            print("Chief: 'Sorry, but we can't cook that'")

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
    def list_ingredients(self) -> None:
        print(f"Salad ingredients: {', '.join(self.ingredients)}", end="")

class Waiter:
    took_order = None
    def took_order(self, order: Order):
        self._took_order = order
    def pass_order(self) -> None:
        if isinstance(self._took_order, Order):
            print("\nWaiter: 'I'm going to tell the Chief about your order'")
            self._took_order.execute()
        print("Waiter: 'Enjoy'")

if __name__ == "__main__":
    waiter = Waiter()
    cook = SaladCook()
    chief = SaladChief(cook)
    waiter.took_order(SaladOrder(chief, "meat salad"))
    waiter.pass_order()
