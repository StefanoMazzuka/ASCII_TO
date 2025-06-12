from element import Element
from entity import Entity
from position import Position
from constants import HEART, PLAYER_SPRITES, RIGHT, PLAYER_MOVEMENTS, EMPTY


class Player(Entity):
    def __init__(self, position: Position, skin: chr, sprites: dict, health: int = 10):
        super().__init__(position, skin, sprites, collision=False)
        self.health = health
        self.bag = {}

    def pick_up(self, item: Element):

        if item.skin == HEART:
            self.heal_player()
        else:
            self.put_in_bag(item)

    def heal_player(self):
        self.health += 1

    def put_in_bag(self, item: Element):
        if item.skin in self.bag:
            self.bag[item.skin] += 1
        else:
            self.bag[item.skin] = 1

        for key, value in self.bag.items():
            print(f"{key}: {value}")