from src.buildings.city import City
from src.buildings.outpost import Outpost
from map import HeightMap, SurfaceMap

from typing import List


class Planet:
    def __init__(self, name: str, custom_name: str,
                 temperature: float, pressure: float, oxygen: float, water: float, biomass: float,
                 population: float, height_map: HeightMap, surface_map: SurfaceMap, cities: List[City] = None,
                 posts: List[Outpost] = None, satellites: List = None):
        self.name = name
        self.custom_name = custom_name
        self.temperature = temperature  # mK
        self.pressure = pressure  # Pa
        self.oxygen = oxygen  # ppm
        self.water = water  # mm
        self.biomass = biomass  # million tons
        self.population = population
        self.height_map = height_map
        self.surface_map = surface_map
        self.cities = cities
        self.posts = posts
        self.satellites = satellites
        if cities is None:
            self.cities = []
        if posts is None:
            self.posts = []
        if satellites is None:
            self.satellites = []

    def get_sea_level(self) -> float:
        standard = 300000
        if self.temperature < 200500 or self.temperature > 399500 or self.pressure < 600:
            return -1.0
        elif 200500 <= self.temperature <= standard:
            return (standard - self.temperature) / (standard - 200500) * self.water
        else:
            return (self.temperature - standard) / (standard - 200500) * self.water

    def get_diff(self) -> List[float]:
        diff = []
        for city in self.cities:
            diff = list(map(lambda x, y: x + y, diff, city.get_diff()))
        return diff

    def tick(self):
        # TODO
        pass


class PlanetProvider:
    def __init__(self,
                 name: str, temperature: float, pressure: float, oxygen: float, water: float, biomass: float,
                 height_map: HeightMap, surface_map: SurfaceMap):
        self.name = name
        self.temperature = temperature  # mK
        self.pressure = pressure  # Pa
        self.oxygen = oxygen  # ppm
        self.water = water  # mm
        self.biomass = biomass  # million tons
        self.population = 0
        self.height_map = height_map
        self.surface_map = surface_map

    def get_planet(self, custom_name: str) -> Planet:
        return Planet(self.name, custom_name, self.temperature, self.pressure, self.oxygen, self.water, self.biomass,
                      self.population, self.height_map, self.surface_map)
