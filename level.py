from constants import PLAYER_SPRITES, ENEMY_SPRITES, RIGHT, WALL
from element import Element
from entity import Entity
from map import Map
from position import Position


class Level:
    def __init__(self):
        self.map      = None
        self.elements = []
        self.player   = None

    def create_map(self, width: int, height: int):
        self.map = Map(width, height)

    def _add_element(self, element_class, *args, **kwargs) -> Element:
        position = self.map.adjust_position_within_bounds(kwargs.get("position"))
        element = element_class(*args, position=position, **kwargs)
        self.map.add_element(element, position)
        self.elements[element.id] = position

        return element

    def add_player(self, position: Position=None):
        self._add_element(Entity, PLAYER_SPRITES[RIGHT], PLAYER_SPRITES, position)

    def add_enemy(self, position: Position=None):
        position = self.map.adjust_position_within_bounds(position)
        enemy = Entity(ENEMY_SPRITES[RIGHT], ENEMY_SPRITES, position)
        self._add_element(enemy, position)

    def add_structure(self, structure_name: chr, position: Position=None):
        position = self.map.adjust_position_within_bounds(position)
        structure = Element(structure_name, position, collision=True)
        self._add_element(structure, position)

    def add_item(self, item_name: chr, position=None):
        position = self.map.adjust_position_within_bounds(position)
        item = Element(item_name, position, pickable=True)
        self._add_element(item, position)

    def move_player(self, direction: tuple[int, int]):
        player = self.entities[]
        next_position = player.position + direction

        if not self.map.out_of_bounds(next_position):
            element = self.map.get_element(next_position)
            if element.pickable:
                self.entities[0].on_top_of = element
            if not element.collision:
                self.map.update_player_position(next_position, self.entities[0])

    def show(self):
        self.map.show()
