from constants import EMPTY, HEART
from element import Element
from position import Position


class Item(Element):
    def __init__(self, position: Position, skin: str, collision: bool = False):
        super().__init__(position, skin, collision)

    def on_collision(self, player):
        player.on_top_of = Element(player.on_top_of.position, EMPTY)
        if self.skin == HEART:
            player.heal_player()
        else:
            player.put_in_bag(self)

        print("Life:", player.health)
