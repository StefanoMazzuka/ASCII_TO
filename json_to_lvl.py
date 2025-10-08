import json
from app_2 import game_loop
from constants import PLAYER_SPRITES, ENEMY_SPRITES, PICKABLES, SOLID_STRUCTURES, NON_SOLID_STRUCTURES
from level import Level
from position import Position


def load_lvls():
    with open(f"resources/levels/lvls.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


lvls = load_lvls()


def load_lvl(lvl_name: str):
    data = lvls[lvl_name]
    width = data['width']
    height = data['height']
    chars = data['chars']
    lvl = Level()
    lvl.create_map(width=width, height=height)

    for chars in data["chars"]:
        for char, coordinates in chars.items():
            pos = Position(coordinates[0], coordinates[1])
            if char in PLAYER_SPRITES.values():
                lvl.add_player(char, pos)
            if char in ENEMY_SPRITES.values():
                lvl.add_enemy(char, pos)
            if char in SOLID_STRUCTURES:
                lvl.add_structure(char, pos)
            if char in NON_SOLID_STRUCTURES:
                lvl.add_structure(char, pos, collision=False)
            if char in PICKABLES:
                lvl.add_item(char, pos)

    return lvl


lvl = load_lvl("lvl_1")
game_loop(lvl)
