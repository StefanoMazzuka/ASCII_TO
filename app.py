import utils
import keyboard

from position import Position
from constants import *

from element import Element
from inventory import Inventory
from map import Map

def play(map, inventory):

    utils.clear_console()
    map.show()
    inventory.show()

    while True:
        event = keyboard.read_event(suppress=True)

        if event.event_type == "down":
            key = event.name

            # Movement
            if key in MOVEMENTS:

                next_position = map.player.get_next_position(MOVEMENTS[key])

                if not map.out_of_bounds(next_position):
                    element = map.get_element(next_position)
                    if element.pickable:
                        inventory.add_item(0, element)
                    p = Element(SPRITES[key])
                    map.update_player_position(next_position, p)
                    utils.clear_console()
                    map.show()
                    inventory.show()

            # Inventory
            if key in ITEMS:
                inventory.selected_item = ITEMS[key]
                utils.clear_console()
                map.show()
                inventory.show()

            elif key == EXIT:
                break

def main():
    map = Map(20, 10)
    map.insert_element(Position(2, 2), Element(WALL, collision=True))
    map.insert_element(Position(4, 2), Element(HEART, pickable=True))
    map.insert_element(Position(4, 5), Element(FLOOR))
    map.insert_element(Position(5, 5), Element(FLOOR))
    inventory = Inventory()
    play(map, inventory)

if __name__ == "__main__":
    main()