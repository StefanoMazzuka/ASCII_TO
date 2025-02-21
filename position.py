from movement import Movement


class Position:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __add__(self, other):
        if isinstance(other, Position):
            self.y += other.y
            self.x += other.x
        if isinstance(other, Movement):
            self.y = Movement