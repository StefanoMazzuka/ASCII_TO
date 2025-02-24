import field as f
import menu
import utils
import keyboard

from PIL import Image
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


def image_to_ascii(image_path, width=195):
    # Open the image
    image = Image.open(image_path)

    # Resize the image
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width)
    image = image.resize((width, new_height))

    # Convert the image to grayscale
    image = image.convert('L')

    # Define ASCII characters
    ascii_chars = "@%#*+=-:. "

    # Convert pixels to ASCII characters
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ascii_chars[pixel // 32]

    # Split the string into lines
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i + width)] for i in range(0, ascii_str_len, width)])

    return ascii_img
def main():

    image_path = 'images/foto_perfil.jpg'
    # Convert image to ASCII
    ascii_image = image_to_ascii(image_path)

    # Print the ASCII image
    print(ascii_image)

    map = Map(20, 10)
    map.insert_element(Position(2, 2), Element(WALL, collision=True))
    map.insert_element(Position(4, 2), Element(HEART, pickable=True))
    map.insert_element(Position(4, 5), Element(FLOOR))
    map.insert_element(Position(5, 5), Element(FLOOR))
    inventory = Inventory()
    play(map, inventory)

if __name__ == "__main__":
    main()