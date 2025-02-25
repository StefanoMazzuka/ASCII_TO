import time

import utils
import keyboard

from inventory import Inventory
from constants import *
from level import Level
from position import Position


def play(level, inventory):

    frame_duration = 1 / 60  # Duration of each frame for 60fps
    utils.clear_console()
    level.show()
    inventory.show()
    for k in level.elements:
        print(f"{k}: {level.elements[k].y}, {level.elements[k].x}")

    while True:
        start_time = time.time()

        for key in PLAYER_MOVEMENTS:
            if keyboard.is_pressed(key):
                print(key)

        for key in ITEMS:
            if keyboard.is_pressed(key):
                inventory.selected_item = ITEMS[key]
                utils.clear_console()
                level.show()
                inventory.show()

        if keyboard.is_pressed(EXIT):
            break

        # event = keyboard.poll_event()
        #
        # if event and event.event_type == "down":
        #     key = event.name
        #
        #     # Movement
        #     if key in PLAYER_MOVEMENTS:
        #
        #         print(key)

                # level.move_player(PLAYER_MOVEMENTS[key])

                # if not map.out_of_bounds(next_position):
                #     element = map.get_element(next_position)
                #     if element.pickable:
                #         inventory.add_item(0, element)
                #     p = Element(SPRITES[key])
                #     map.update_player_position(next_position, p)
                #     utils.clear_console()
                #     map.show()
                #     inventory.show()

            # Inventory
            # if key in ITEMS:
            #
            #
            # elif key == EXIT:
            #     break

        # Calculate the time taken for this frame
        elapsed_time = time.time() - start_time
        # Sleep for the remaining time to maintain 60fps
        time.sleep(max(0, frame_duration - elapsed_time))

def main():
    level_1 = Level()
    level_1.create_map(width=20, height=10)
    level_1.add_player()
    level_1.add_enemy(Position(1, 1))
    level_1.add_structure(WALL, Position(2, 2))
    level_1.add_structure(WALL, Position(3, 2))
    level_1.add_item(HEART, Position(1, 6))
    level_1.add_structure(FLOOR, Position(4, 5))
    level_1.add_structure(FLOOR, Position(5, 5))
    inventory = Inventory()
    play(level_1, inventory)

if __name__ == "__main__":
    main()