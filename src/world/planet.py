from typing import List

from src.buildings.city import City
from src.buildings.outpost import Outpost


class Planet:
    def __init__(self,
                 name: str, temperature: float, pressure: float, oxygen: float, water: float, biomass: float,
                 population: int, cities: List[City] = None, posts: List[Outpost] = None
                 ):
        self.posts = posts
        self.population = population
        self.water = water  # mm
        self.temperature = temperature  # mK
        self.pressure = pressure  # Pa
        self.oxygen = oxygen  # ppm
        self.biomass = biomass  # million tons
        self.cities = cities
        self.name = name
        if cities is None:
            self.cities = []
        if posts is None:
            self.posts = []
