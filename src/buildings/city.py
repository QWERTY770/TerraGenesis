from src.util.coordinate import Coordinate2D
from faci import Faci
from src.events.effect import Effect
from src.core.constants import TICKING_SPEED

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
        return max(result, 25)

    def can_build_faci(self) -> bool:
        return len(self.faci_list) < self.get_max_facis()

    def add_faci(self, faci: Faci):
        self.faci_list.append(faci)

    def remove_faci(self, faci: Faci):
        self.faci_list.remove(faci)

    def add_effect(self, effect: Effect):
        self.effect_list.append(effect)

    def get_diff(self) -> List[float]:
        diff = [0, 0, 0, 0, 0, 0, 0]
        for zh in self.faci_list:
            diff[0] += zh.temp_gen
            diff[1] += zh.pressure_gen
            diff[2] += zh.oxygen_gen
            diff[3] += zh.water_gen
            diff[4] += zh.biomass_gen
            diff[5] += zh.pop_gen
            diff[6] += zh.money_gen
        for zh in self.effect_list:
            diff[5] += zh.pop_gen
            diff[6] += zh.money_gen
        return list(map(lambda zhh: zhh / TICKING_SPEED, diff))

    def pop_limit(self):
        return sum([i.pop_limit for i in self.faci_list])

    def tick(self):
        self.pop = max(self.pop + self.get_diff()[5], self.pop_limit())
