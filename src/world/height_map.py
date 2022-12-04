from src.util.coordinate import Coordinate2D
import numpy


class HeightMap:
    def __init__(self, array: numpy.ndarray):
        self.array = array

    def get_height_at(self, pos: Coordinate2D):
        return self.array[pos.x, pos.y]
