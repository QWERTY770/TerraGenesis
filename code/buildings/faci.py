import json


class BaseFaci:
    def __init__(self, name: str, description: str, faci_id: int, faci_type: str, faci_tier: int,
                 temp_gen, pressure_gen, oxygen_gen, water_gen, biomass_gen, pop_gen, money_gen,
                 pop_max: int = 0):
        self.name = name  # translation key, not real name
        self.description = description  # translation key, not real name
        self.id = faci_id
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


class Faci:
    def __init__(self, basefaci: BaseFaci, max_level: int, level: int, cost_multiplier: int = 1):
        self.basefaci = basefaci
        self.max_level = max_level
        self.level = level
        self.cost_multiplier = cost_multiplier

    def get_maintenance_cost(self):
        return self.basefaci.tier * self.level * 500 * self.cost_multiplier

    @property
    def temp_gen(self):
        return self.basefaci.temp_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pressure_gen(self):
        return self.basefaci.pressure_gen * (1 + (self.level - 1) * 0.5)

    @property
    def oxygen_gen(self):
        return self.basefaci.oxygen_gen * (1 + (self.level - 1) * 0.5)

    @property
    def water_gen(self):
        return self.basefaci.water_gen * (1 + (self.level - 1) * 0.5)

    @property
    def biomass_gen(self):
        return self.basefaci.biomass_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pop_gen(self):
        return self.basefaci.pop_gen * (1 + (self.level - 1) * 0.5)

    @property
    def pop_max(self):
        return self.basefaci.pop_max * (1 + (self.level - 1) * 0.5)

    @property
    def money_gen(self):
        return self.basefaci.money_gen * (1 + (self.level - 1) * 0.5)


def json_to_faci(src: dict):
    t1 = src["data"]
    try:
        t2 = t1["pop_max"]
        return BaseFaci(src["name"], src["description"], src["id"], src["type"], src["tire"],
                        t1["temp_gen"], t1["pressure_gen"], t1["oxygen_gen"], t1["water_gen"],
                        t1["biomass_gen"], t1["pop_gen"], t1["money_gen"], t2)
    except KeyError:
        return BaseFaci(src["name"], src["description"], src["id"], src["type"], src["tire"],
                        t1["temp_gen"], t1["pressure_gen"], t1["oxygen_gen"], t1["water_gen"],
                        t1["biomass_gen"], t1["pop_gen"], t1["money_gen"])


if __name__ == "__main__":
    a = json_to_faci(json.loads(open(r"../../data/teg/facilities/heating_cluster.json").read()))
    b = Faci(a, 2, 5)
    print(b.temp_gen)
    print(b.pressure_gen)
    print(b.get_maintenance_cost())
    print(b.basefaci.description)
