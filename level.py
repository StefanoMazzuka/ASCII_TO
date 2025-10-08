import random

from constants import PLAYER_SPRITES, ENEMY_SPRITES, RIGHT, PLAYER_MOVEMENTS, DIRECTIONS, DIAMOND
from element import Element
from enemy import Enemy
from item import Item
from map import Map
from player import Player
from position import Position


class Level:
    def __init__(self, player: Player = None):
        self.map = None
        self.elements = {}
        self.player = Player if player is None else player

    def create_map(self, width: int, height: int):
        self.map = Map(width, height)

    def _add_element(self, element_class, **kwargs) -> Element:
        kwargs["position"] = self.map.adjust_position_within_bounds(kwargs.get("position"))
        element = element_class(**kwargs)
        self.map.add_element(element, element.position)
        self.elements[element.id] = element

        return element

    def add_player(self, skin: str, position: Position = None, ):
        self.player = self._add_element(Player, position=position, skin=skin, sprites=PLAYER_SPRITES)

    def add_enemy(self, skin: str, position: Position = None, health: int = 5, drops=None):
        drops = {None, 1.0} if drops is None else drops
        self._add_element(Enemy, position=position, skin=skin, sprites=ENEMY_SPRITES, health=health, drops=drops)

    def add_structure(self, skin: str, position: Position = None, collision=True):
        self._add_element(Element, position=position, skin=skin, collision=collision)

    def add_item(self, skin: str, position=None):
        self._add_element(Item, position=position, skin=skin)

    def move_player(self, key: str):

        direction = PLAYER_MOVEMENTS[key]
        self.player.skin = PLAYER_SPRITES[key]
        self.map.add_element(self.player, self.player.position)

        next_position = self.player.position + direction

        if not self.map.out_of_bounds(next_position):
            element = self.map.get_element(next_position)

            if isinstance(element, Enemy):
                self.player.health -= 1
                print("Player encountered an enemy! player health:", self.player.health)

            if not element.collision:
                self.map.add_element(self.player.on_top_of, self.player.position)
                self.player.position = next_position
                self.map.add_element(self.player, self.player.position)
                self.player.on_top_of = element

                element.on_collision(self.player)

        else:
            print("Out of bounds!")
        print("player position:", self.player.position.x, self.player.position.y)
        print("player on top of:", self.player.on_top_of.skin)

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
                    if isinstance(next_element, Player):
                        next_element.health -= 1
                        print("Enemy encountered the player! Player health:", next_element.health)


def __str__(self):
    return str(self.map)
