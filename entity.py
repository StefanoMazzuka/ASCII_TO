from constants import EMPTY
from element import Element


class Entity(Element):
    def __init__(self, skin, sprites):
        super().__init__(skin)
        self.sprites   = sprites
        self.on_top_of = Element(EMPTY)
