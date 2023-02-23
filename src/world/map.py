from typing import Tuple

from src.util.coordinate import Coordinate2D

import numpy as np
from PIL import Image


class HeightMap:
    def __init__(self, array: np.ndarray):
        self.array = array

    @classmethod
    def from_image(cls, file: str):
        img = Image.open(file)
        orig_map = np.array(img)
        gray_map = 0.2989 * orig_map[:, :, 0] + 0.587 * orig_map[:, :, 1] + 0.114 * orig_map[:, :, 2]
        return HeightMap(gray_map.astype(np.uint8))

    def height_at(self, pos: Coordinate2D) -> float:
        try:
            return self.array[pos.x, pos.y]
        except IndexError:
            return -1.0

    def size(self) -> Tuple[int, int]:
        rows = len(self.array)
        if rows == 0:
            return 0, 0
        columns = len(self.array[0])
        return rows, columns


class SurfaceMap:
    def __init__(self):
        pass
