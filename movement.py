from entity import Entity
from position import Position

class Movement:
    def __init__(self, entity: Entity, direction):
        value_y = entity.get_position().y + direction[0]
        value_x = entity.get_position().x + direction[1]
        self.position = Position(value_y, value_x)