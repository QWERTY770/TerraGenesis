import random


class Effect:
    def __init__(self, effect_id: int, name: str, description: str, pop_gen, money_gen):
        self.id = effect_id
        self.name = name
        self.description = description
        self.pop_gen = pop_gen
        self.money_gen = money_gen


def get_random_value():
    return 0.8 + 0.4 * random.random()


revenue_low = Effect(1, "effect.vanilla.revenue_low", "effect.vanilla.revenue_low", 0, 1500 * get_random_value())
revenue_middle = Effect(1, "effect.vanilla.revenue_low", "effect.vanilla.revenue_low", 0, 1500 * get_random_value())
revenue_high = Effect(1, "effect.vanilla.revenue_low", "effect.vanilla.revenue_low", 0, 1500 * get_random_value())
