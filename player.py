from constants import PLAYER
from element import Element

class Player(Element):
    def __init__(self, position):
        super().__init__(PLAYER)
        self.position = position

    def get_position(self):
        return self.position

    def get_next_position(self, movement):
        return self.position + movement