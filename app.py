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
    frame_duration = 1 / 10  # Duration of each frame for 10fps
    enemy_velocity = 1
    player_velocity = 0.25
    enemy_start_time = time.time()
    player_start_time = time.time()

    while True:
        current_time = time.time()

        if current_time - enemy_start_time >= enemy_velocity:
            level.move_enemies()
            enemy_start_time = current_time

        if current_time - player_start_time >= player_velocity:
            for key in PLAYER_MOVEMENTS:
                if keyboard.is_pressed(key):
                    level.move_player(key)
                    player_start_time = current_time

        for key in ITEMS:
            if keyboard.is_pressed(key):
                inventory.selected_item = ITEMS[key]

        if keyboard.is_pressed(EXIT):
            break

        update_view(level, inventory)

        # Calculate the time taken for this frame
        elapsed_time = time.time() - current_time
        time.sleep(max(0, int(frame_duration - elapsed_time)))


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
