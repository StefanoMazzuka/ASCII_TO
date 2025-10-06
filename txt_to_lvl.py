from app_2 import game_loop
from constants import PLAYER_SPRITES, ENEMY_SPRITES, PICKABLES, SOLID_STRUCTURES, NON_SOLID_STRUCTURES
from level import Level
from position import Position


def read_txt(lvl_file: str):
    with open(f"resources/levels/{lvl_file}.txt", "r", encoding='utf-8') as file:
        chars = [line.strip('\n') for line in file.readlines()]

    return chars


def create_lvl():
    chars  = read_txt("lvl_1")
    width  = len(chars[0])
    height = len(chars)
    lvl = Level()
    lvl.create_map(width=width, height=height)

    for y, row in enumerate(chars):
        for x, char in enumerate(row):

            if char in PLAYER_SPRITES.values():
                lvl.add_player(char, Position(y, x))
            if char in ENEMY_SPRITES.values():
                lvl.add_enemy(char, Position(y, x))
            if char in SOLID_STRUCTURES:
                lvl.add_structure(char, Position(y, x))
            if char in NON_SOLID_STRUCTURES:
                lvl.add_structure(char, Position(y, x), collision=False)
            if char in PICKABLES:
                lvl.add_item(char, Position(y, x))

    return lvl


lvl = create_lvl()
game_loop(lvl)
