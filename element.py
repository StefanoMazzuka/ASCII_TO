import uuid

from position import Position


class Element:
    def __init__(self, position: Position, skin: chr, collision: bool=False, pickable: bool=False):
        self.position  = position
        self.skin      = skin
        self.collision = collision
        self.pickable  = pickable
        self.id        = uuid.uuid4()
