from entity import Entity
from position import Position


class Player(Entity):
    def __init__(self, position: Position, skin: chr, sprites: dict, health: int = 10):
        super().__init__(position, skin, sprites)
        self.health = health

