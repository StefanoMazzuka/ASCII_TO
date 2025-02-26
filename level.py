import random

from constants import PLAYER_SPRITES, ENEMY_SPRITES, RIGHT, PLAYER_MOVEMENTS, DIRECTIONS
from element import Element
from enemy import Enemy
from entity import Entity
from map import Map
from position import Position


class Level:
    def __init__(self):
        self.map = None
        self.elements = {}
        self.player = None

    def create_map(self, width: int, height: int):
        self.map = Map(width, height)

    def _add_element(self, element_class, **kwargs) -> Element:
        kwargs["position"] = self.map.adjust_position_within_bounds(kwargs.get("position"))
        element = element_class(**kwargs)
        self.map.add_element(element, element.position)
        self.elements[element.id] = element

        return element

    def add_player(self, position: Position = None):
        self.player = self._add_element(Entity, position=position, skin=PLAYER_SPRITES[RIGHT], sprites=PLAYER_SPRITES)

    def add_enemy(self, position: Position = None, health: int = 5, drops=None):
        drops = {None, 1.0} if drops is None else drops
        self._add_element(Enemy, position=position, skin=ENEMY_SPRITES[DIRECTIONS[0]], sprites=ENEMY_SPRITES,
                          health=health, drops=drops)

    def add_structure(self, structure_skin: chr, position: Position = None, collision=True):
        self._add_element(Element, position=position, skin=structure_skin, collision=collision)

    def add_item(self, item_skin: chr, position=None):
        self._add_element(Element, position=position, skin=item_skin, pickable=True)

    def move_player(self, key: chr):

        direction = PLAYER_MOVEMENTS[key]
        self.player.skin = PLAYER_SPRITES[key]
        self.map.add_element(self.player, self.player.position)

        next_position = self.player.position + direction
        next_position = self.map.adjust_position_within_bounds(next_position)

        element = self.map.get_element(next_position)
        if not element.collision:
            self.map.add_element(self.player.on_top_of, self.player.position)
            self.player.position = next_position
            self.map.add_element(self.player, self.player.position)

            if not element.pickable:
                self.player.on_top_of = element

    def move_enemies(self):
        for key in self.elements:
            element = self.elements[key]
            if isinstance(element, Enemy):
                direction = random.choice(DIRECTIONS)
                element.skin = ENEMY_SPRITES[direction]
                self.map.add_element(element, element.position)

                next_position = element.position + direction
                next_position = self.map.adjust_position_within_bounds(next_position)
                next_element  = self.map.get_element(next_position)

                if not next_element.collision:
                    self.map.add_element(element.on_top_of, element.position)
                    element.position = next_position
                    element.on_top_of = next_element
                    self.map.add_element(element, element.position)

    def __str__(self):
        return str(self.map)
