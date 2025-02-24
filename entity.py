from constants import PLAYER
from element import Element

class Entity(Element):
    def __init__(self, skin, position):
        super().__init__(skin)
        self.position = position

    def get_position(self):
        return self.position

    def get_next_position(self, movement):
        return self.position + movement