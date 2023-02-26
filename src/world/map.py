from typing import Tuple

from src.registry.registry import HasID
from src.util.coordinate import Coordinate2D

import numpy as np
from PIL import Image


class HeightMap(HasID):
    def __init__(self, map_id, array: np.ndarray):
        super().__init__(map_id)
        self.array = array  # 2-dimension array

    @classmethod
    def from_image(cls, map_id, file: str):
        img = Image.open(file)
        orig_map = np.array(img)
        gray_map = 0.2989 * orig_map[:, :, 0] + 0.587 * orig_map[:, :, 1] + 0.114 * orig_map[:, :, 2]
        return HeightMap(map_id, gray_map.astype(np.uint8))

    def get_height_at(self, pos: Coordinate2D) -> int:
        try:
            return self.array[pos.x, pos.y]
        except IndexError:
            return -1

    def size(self) -> Tuple[int, int]:
        return self.array.size


class SurfaceMap(HasID):
    def __init__(self, map_id, array: np.ndarray):
        super().__init__(map_id)
        self.array = array  # 3-dimension array

    @classmethod
    def from_image(cls, map_id, file: str):
        img = Image.open(file)
        orig_map = np.array(img)
        return HeightMap(map_id, orig_map.astype(np.uint8))

    def size(self) -> Tuple[int, int, int]:
        return self.array.size
