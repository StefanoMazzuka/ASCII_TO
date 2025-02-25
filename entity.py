from constants import EMPTY
from position import Position
from element import Element


class Entity(Element):
    def __init__(self, skin: str, sprites: dict, position: Position):
        super().__init__(skin, position)
        self.sprites   = sprites
        self.on_top_of = Element(EMPTY, position)
