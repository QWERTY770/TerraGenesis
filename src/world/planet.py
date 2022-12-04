from src.buildings.city import City
from src.buildings.outpost import Outpost
from height_map import HeightMap

from typing import List


class BasePlanet:
    def __init__(self,
                 name: str, temperature: float, pressure: float, oxygen: float, water: float, biomass: float,
                 population: int, height_map: HeightMap, cities: List[City] = None, posts: List[Outpost] = None
                 ):
        self.name = name
        self.temperature = temperature  # mK
        self.pressure = pressure  # Pa
        self.oxygen = oxygen  # ppm
        self.biomass = biomass  # million tons
        self.population = population
        self.water = water  # mm
        self.height_map = height_map
        self.cities = cities
        self.posts = posts
        if cities is None:
            self.cities = []
        if posts is None:
            self.posts = []

    def get_diff(self) -> List[float]:
        diff = []
        for city in self.cities:
            diff = list(map(lambda x, y: x + y, diff, city.get_diff()))
        return diff

    def tick(self):
        # TODO
        pass


class Planet:
    def __init__(self, base_planet: BasePlanet, custom_name: str, cities: List[City] = None,
                 posts: List[Outpost] = None):
        # TODO
        pass
