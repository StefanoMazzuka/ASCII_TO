import uuid

from position import Position


class Element:
    def __init__(self, skin: chr, position: Position, collision: bool=False, pickable: bool=False):
        self.skin      = skin
        self.position  = position
        self.collision = collision
        self.pickable  = pickable
        self.id        = uuid.uuid4()
