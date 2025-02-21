from constants import NUM_ITEMS, EMPTY
from element import Element


class Inventory:
    def __init__(self):
        self.items = [Element(EMPTY)] * NUM_ITEMS
        self.selected_item = 0

    def add_item(self, index, element):
        self.items[index] = element

    def remove_item(self, element):
        self.items.remove(element)

    def get_items(self):
        return self.items

    def show(self):
        top, mid, bottom = "", "", ""
        for i, element in enumerate(self.items):
            if i == self.selected_item:
                top += "╔═══╗"
                mid += f"║ {element.skin} ║"
                bottom += "╚═══╝"
            else:
                top += "┌───┐"
                mid += f"│ {element.skin} │"
                bottom += "└───┘"

        print(top)
        print(mid)
        print(bottom)
