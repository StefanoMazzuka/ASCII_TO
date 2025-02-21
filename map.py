from position import Position
from constants import EMPTY

from element import Element
from player import Player

class Map:
    def __init__(self, width, height):
        self.width        = width
        self.height       = height
        self.matrix       = [[Element(EMPTY) for _ in range(width)] for _ in range(height)]
        self.last_element = Element(EMPTY)

        self.player = Player(Position(int(height / 2), int(width / 2)))
        self.matrix[self.player.position.y][self.player.position.x] = self.player

    def size(self):
        return self.width, self.height

    def print_top(self):
        print("┏" + "━" * (self.width) + "┓")

    def print_bottom(self):
        print("┗" + "━" * (self.width) + "┛")

    def show(self):
        self.print_top()#█◘░▒▓█
        for row in self.matrix:
            print("┃" + "".join(str(element.skin) for element in row) + "┃")
        self.print_bottom()

    def out_of_bounds(self, position):
        return not (0 <= (self.player.position.y + position.y) < self.height and 0 <= (self.player.position.x + position.x) < self.width)

    def update_player_position(self, position, p):
        self.matrix[self.player.position.y][self.player.position.x] = p

        next_position = self.player.position + position
        next_element = self.get_element(next_position)

        if not next_element.collision:
            self.matrix[self.player.position.y][self.player.position.x] = self.last_element

            self.player.position.x = max(0, min(self.player.position.x + position.x, self.width - 1))
            self.player.position.y = max(0, min(self.player.position.y + position.y, self.height - 1))

            self.last_element = self.get_element(self.player.position)
            self.matrix[self.player.position.y][self.player.position.x] = p

    def insert_element(self, position, element):
        self.matrix[position.y][position.x] = element

    def get_element(self, position):
        return self.matrix[position.y][position.x]