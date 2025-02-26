class Position:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def __add__(self, other):
        added_y = self.y
        added_x = self.x
        if isinstance(other, Position):
            added_y += other.y
            added_x += other.x
        if isinstance(other, tuple):
            added_y += other[0]
            added_x += other[1]

        return Position(added_y, added_x)