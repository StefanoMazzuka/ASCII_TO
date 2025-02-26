import time

import utils
import keyboard

from inventory import Inventory
from constants import *
from level import Level
from position import Position


def update_view(level, inventory):
    utils.clear_console()
    print(str(level))
    print(str(inventory))


def play(level, inventory):
    update_view(level, inventory)

    enemy_speed  = 1.0
    player_speed = 4.0

    last_time = time.perf_counter()

    enemy_accumulator = 0
    player_accumulator = 0

    while True:
        current_time = time.perf_counter()
        delta_time = current_time - last_time
        last_time = current_time

        enemy_accumulator  += delta_time
        player_accumulator += delta_time

        if enemy_accumulator >= 1 / enemy_speed:
            level.move_enemies()
            enemy_accumulator = 0

        if player_accumulator >= 1 / player_speed:
            for key in PLAYER_MOVEMENTS:
                if keyboard.is_pressed(key):
                    level.move_player(key)
                    player_accumulator = 0

        for key in ITEMS:
            if keyboard.is_pressed(key):
                inventory.selected_item = ITEMS[key]

        if keyboard.is_pressed(EXIT):
            break

        update_view(level, inventory)


def block_keys():
    for key in BUTTONS:
        keyboard.block_key(key)


def main():
    block_keys()
    level_1 = Level()
    level_1.create_map(width=10, height=10)
    level_1.add_player()
    level_1.add_enemy(Position(1, 1))
    level_1.add_enemy(Position(3, 11))
    level_1.add_item(HEART, Position(1, 2))
    level_1.add_structure(WALL, Position(2, 2))
    level_1.add_structure(WALL, Position(3, 2))
    level_1.add_structure(FLOOR, Position(4, 5), collision=False)
    level_1.add_structure(FLOOR, Position(3, 5), collision=False)
    inventory = Inventory()
    play(level_1, inventory)


if __name__ == "__main__":
    main()
