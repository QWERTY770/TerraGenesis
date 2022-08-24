from code.api.coordinate import Coordinate2D
from faci import Faci
from code.events.effect import Effect
from typing import List


class City:
    def __init__(self, name: str, pos: Coordinate2D, faci_list: List[Faci], effect_list: List[Effect]):
        self.name = name
        self.pos = pos
        self.faci_list = faci_list
        self.effect_list = effect_list
        self.pop = 0

    def get_max_facis(self) -> int:
        result = 2
        t = self.pop // 50
        while t != 0:
            result += 1
            t = t >> 1
        return max(result, 20)

    def can_build_faci(self) -> bool:
        return len(self.faci_list) < self.get_max_facis()

    def add_faci(self, faci: Faci):
        self.faci_list.append(faci)

    def remove_faci(self, faci: Faci):
        self.faci_list.remove(faci)

    def add_effect(self, effect: Effect):
        self.effect_list.append(effect)

    def tick(self):
        pass


class Post:
    def __init__(self):
        pass
