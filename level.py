from constants import PLAYER_SPRITES, ENEMY_SPRITES, RIGHT, WALL
from element import Element
from entity import Entity
from map import Map


class Level:
    def __init__(self):
        self.map             = None
        self.entities        = []
        self.player_position = None

    def create_map(self, width, height):
        self.map = Map(width, height)

    def _add_element(self, element, position=None):
        self.map.add_element(element, position)
        self.entities.append(element)

    def add_player(self, position=None):
        player = Entity(skin=PLAYER_SPRITES[RIGHT], sprites=PLAYER_SPRITES)
        self._add_element(player, position)
        self.player

    def add_enemy(self, position=None):
        enemy = Entity(skin=ENEMY_SPRITES[RIGHT], sprites=ENEMY_SPRITES)
        self._add_element(enemy, position)

    def add_structure(self, structure_name, position=None):
        structure = Element(skin=structure_name, collision=True)
        self._add_element(structure, position)

    def add_item(self, item_name, position=None):
        item = Element(skin=item_name, pickable=True)
        self._add_element(item, position)

    def move_player(self, direction):
        player = self.entities[0]
        next_position = player.position + direction

        if not self.map.out_of_bounds(next_position):
            element = self.map.get_element(next_position)
            if element.pickable:
                self.entities[0].on_top_of = element
            if not element.collision:
                self.map.update_player_position(next_position, self.entities[0])

    def show(self):
        self.map.show()
