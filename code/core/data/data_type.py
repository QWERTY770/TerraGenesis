import random
from typing import Union


class NumberData:
    def __init__(self, value: Union[int, float, None]):
        self.value = value

    def get_value(self):
        if self.value is None:
            raise ValueError("value is None")
        return self.value


class RandomIntData(NumberData):
    def __init__(self, min_v, max_v):
        super().__init__(None)
        self.min = min_v
        self.max = max_v

    def get_value(self):
        self.value = random.randint(self.min, self.max)
        return super(RandomIntData, self).get_value()


class RandomFloatData(NumberData):
    def __init__(self, min_v, max_v):
        super().__init__(None)
        self.min = min_v
        self.max = max_v

    def get_value(self):
        self.value = random.uniform(self.min, self.max)
        return super(RandomFloatData, self).get_value()
