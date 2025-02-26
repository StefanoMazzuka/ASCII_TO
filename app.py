import time

import utils
import keyboard

from inventory import Inventory
from constants import *
from level import Level
from position import Position


def play(level, inventory):

    frame_duration = 1 / 10  # Duration of each frame for 30fps
    utils.clear_console()
    level.show()
    inventory.show()

    while True:
        start_time = time.time()
        level.move_enemies()
        for key in PLAYER_MOVEMENTS:
            if keyboard.is_pressed(key):
                level.move_player(key)

        for key in ITEMS:
            if keyboard.is_pressed(key):
                inventory.selected_item = ITEMS[key]

        if keyboard.is_pressed(EXIT):
            break

        utils.clear_console()
        level.show()
        inventory.show()

        # Calculate the time taken for this frame
        elapsed_time = time.time() - start_time
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
    level_1.add_item(HEART, Position(1, 2))
    level_1.add_structure(WALL, Position(2, 2))
    level_1.add_structure(WALL, Position(3, 2))
    level_1.add_structure(FLOOR, Position(4, 5), collition=False)
    level_1.add_structure(FLOOR, Position(3, 5), collition=False)
    inventory = Inventory()
    play(level_1, inventory)


if __name__ == "__main__":
    main()
