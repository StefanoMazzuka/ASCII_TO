from constants import EMPTY
from position import Position
from element import Element


class Entity(Element):
    def __init__(self, position: Position, skin: chr, sprites: dict):
        super().__init__(position, skin, collision=True)
        self.sprites   = sprites
        self.on_top_of = Element(position, EMPTY)
