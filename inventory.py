from constants import NUM_ITEMS, EMPTY
from element import Element


class Inventory:
    def __init__(self):
        self.items = [EMPTY] * NUM_ITEMS
        self.selected_item = 0

    def add_item(self, index: int, element: Element):
        self.items[index] = element

    def remove_item(self, element: Element):
        self.items.remove(element)

    def get_items(self) -> list[Element]:
        return self.items

    def show(self):
        top, mid, bottom = "", "", ""
        for i, item in enumerate(self.items):
            if i == self.selected_item:
                top += "╔═══╗"
                mid += f"║ {item} ║"
                bottom += "╚═══╝"
            else:
                top += "┌───┐"
                mid += f"│ {item} │"
                bottom += "└───┘"

        print(top)
        print(mid)
        print(bottom)
