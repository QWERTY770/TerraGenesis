class Coordinate2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def from_subscriptable(subscriptable):
        return Coordinate2D(subscriptable[0], subscriptable[1])

    def add_xy(self, dx: int, dy: int):
        return Coordinate2D(self.x + dx, self.y + dy)

    def add_x(self, dx: int):
        return self.add_xy(dx, 0)

    def add_y(self, dy: int):
        return self.add_xy(0, dy)

    def get_distance(self, other) -> float:
        return (abs(self.x - other.x) + abs(self.y + other.y)) ** 0.5

    def as_list(self) -> list:
        return [self.x, self.y]

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __iter__(self):
        return self.as_list()
