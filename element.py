class Element:
    def __init__(self, skin, sprites, collision=False, pickable=False):
        self.skin      = skin
        self.sprites   = sprites
        self.collision = collision
        self.pickable  = pickable