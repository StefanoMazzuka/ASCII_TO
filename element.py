import uuid

from position import Position

class Element:
    def __init__(self, position: Position, skin: str, collision: bool=False):
        self.position  = position
        self.skin      = skin
        self.collision = collision
        self.id        = uuid.uuid4()

    def on_collision(self, player):
        pass
