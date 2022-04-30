from typing import Optional, Dict
from types import FunctionType
from effect import Effect
from code.buildings.city import City
from random import sample, randint
from code.core.exceptions import *


class Event:
    def __init__(self, name: str, description: str, choices_and_effects: Optional[Dict[str, FunctionType]]):
        self.choices_and_effects = choices_and_effects
        self.name = name
        self.description = description


def empty():
    pass


def randomly_destroy_faci(city: City, count: int = 1):
    if len(city.faci_list) < count or count < 0:
        raise BuildingCountError("wrong building count: expected 0~" + f"{len(city.faci_list)}")
    city.remove_faci(sample(city.faci_list, k=count)[0])


def set_building_grade(city: City, level: int, faci=None):
    if faci is None:
        f = randint(0, len(city.faci_list) - 1)
        city.faci_list[f].level = level


def add_effect(city: City, effect: Effect):
    city.add_effect(effect)
