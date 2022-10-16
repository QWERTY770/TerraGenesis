import json


class BaseFaci:
    def __init__(self, faci_id: int, name: str, description: str, faci_type: str, faci_tier: int,
                 temp_gen, pressure_gen, oxygen_gen, water_gen, biomass_gen, pop_gen, money_gen,
                 pop_max: int = 0):
        self.id = faci_id
        self.name = name  # translation key, not real name
        self.description = description  # translation key, not real name
        self.type = faci_type
        self.tier = faci_tier
        self.temp_gen = temp_gen
        self.pressure_gen = pressure_gen
        self.oxygen_gen = oxygen_gen
        self.water_gen = water_gen
        self.biomass_gen = biomass_gen
        self.pop_gen = pop_gen
        self.money_gen = money_gen
        self.pop_max = pop_max  # max population in it, set to 0 for non-residential buildings

    @classmethod
    def from_json(cls, src: dict):
        t1 = src["data"]
        try:
            t2 = t1["pop_max"]
            return cls(src["name"], src["description"], src["id"], src["type"], src["tire"],
                       t1["temp_gen"], t1["pressure_gen"], t1["oxygen_gen"], t1["water_gen"],
                       t1["biomass_gen"], t1["pop_gen"], t1["money_gen"], t2)
        except KeyError:
            return cls(src["name"], src["description"], src["id"], src["type"], src["tire"],
                       t1["temp_gen"], t1["pressure_gen"], t1["oxygen_gen"], t1["water_gen"],
                       t1["biomass_gen"], t1["pop_gen"], t1["money_gen"])


class Faci:
    def __init__(self, base_faci: BaseFaci, max_level: int, level: int, cost_multiplier: int = 1):
        self.base_faci = base_faci
        self.max_level = max_level
        self.level = level
        self.cost_multiplier = cost_multiplier

    def get_maintenance_cost(self):
        return self.base_faci.tier * self.level * 500 * self.cost_multiplier

    @property
    def temp_gen(self):
        return self.base_faci.temp_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pressure_gen(self):
        return self.base_faci.pressure_gen * (1 + (self.level - 1) * 0.5)

    @property
    def oxygen_gen(self):
        return self.base_faci.oxygen_gen * (1 + (self.level - 1) * 0.5)

    @property
    def water_gen(self):
        return self.base_faci.water_gen * (1 + (self.level - 1) * 0.5)

    @property
    def biomass_gen(self):
        return self.base_faci.biomass_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pop_gen(self):
        return self.base_faci.pop_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pop_max(self):
        return self.base_faci.pop_max * (1 + (self.level - 1) * 0.5)

    @property
    def money_gen(self):
        return self.base_faci.money_gen * (1 + (self.level - 1) * 0.5)


if __name__ == "__main__":
    a = BaseFaci.from_json(json.loads(open(r"../../resources/data/vanilla/facilities/heating_cluster.json").read()))
    b = Faci(a, 2, 5)
    print(b.temp_gen)
    print(b.pressure_gen)
    print(b.get_maintenance_cost())
    print(b.base_faci.description)
