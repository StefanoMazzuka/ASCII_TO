from constants import PLAYER_SPRITES, ENEMY_SPRITES, RIGHT, WALL, PLAYER_MOVEMENTS
from element import Element
from entity import Entity
from map import Map
from position import Position


class Level:
    def __init__(self):
        self.map      = None
        self.elements = {}
        self.player   = None

    def create_map(self, width: int, height: int):
        self.map = Map(width, height)

    def _add_element(self, element_class, **kwargs) -> Element:
        kwargs["position"] = self.map.adjust_position_within_bounds(kwargs.get("position"))
        element = element_class(**kwargs)
        self.map.add_element(element, kwargs.get("position"))
        self.elements[element.id] = kwargs.get("position")

        return element

    def add_player(self, position: Position=None):
        self.player = self._add_element(Entity, position=position, skin=PLAYER_SPRITES[RIGHT], sprites=PLAYER_SPRITES)

    def add_enemy(self, position: Position=None):
        self._add_element(Entity, position=position, skin=ENEMY_SPRITES[RIGHT], sprites=ENEMY_SPRITES)

    def add_structure(self, structure_skin: chr, position: Position=None, collition=True):
        self._add_element(Element, position=position, skin=structure_skin, collision=collition)

    def add_item(self, item_skin: chr, position=None):
        self._add_element(Element, position=position, skin=item_skin, pickable=True)

    def move_player(self, key: chr):

        direction = PLAYER_MOVEMENTS[key]
        print(type(direction))
        self.player.skin = PLAYER_SPRITES[key]
        self.map.add_element(self.player, self.player.position)

        next_position = self.player.position + direction

        if not self.map.out_of_bounds(next_position):
            element = self.map.get_element(next_position)
            if not element.collision:
                self.map.add_element(self.player.on_top_of, self.player.position)
                self.player.position = next_position
                self.map.add_element(self.player, self.player.position)
                if not element.pickable:
                    self.player.on_top_of = element

    def show(self):
        self.map.show()
