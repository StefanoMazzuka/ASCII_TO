from constants import EMPTY
from position  import Position
from element   import Element


class Map:
    def __init__(self, width, height):
        self.width        = width
        self.height       = height
        self.matrix       = [[Element(EMPTY) for _ in range(width)] for _ in range(height)]
        self.last_element = Element(EMPTY)

        self.center_position = Position(int(height / 2), int(width / 2))

    def add_element(self, element, position):
        """Insert an element in the map."""
        if position is None:
            position = self.center_position

        if self.out_of_bounds(position):
            position = self.adjust_position_within_bounds(position)

        self.matrix[position.y][position.x] = element

    def get_size(self):
        return self.width, self.height

    def _print_top(self):
        print("┏" + "━" * (self.width) + "┓")

    def _print_bottom(self):
        print("┗" + "━" * (self.width) + "┛")

    def show(self):
        """Print the map."""
        self._print_top()
        for row in self.matrix:
            print("┃" + "".join(str(element.skin) for element in row) + "┃")
        self._print_bottom()

    def out_of_bounds(self, position):
        """Check if the position is out of bounds."""
        return not (0 <= position.y < self.height and 0 <= position.x < self.width)

    def adjust_position_within_bounds(self, position):
        """Adjust the position to be within the bounds of the map."""
        adjusted_position_y = position.y = max(0, min(position.y, self.height - 1))
        adjusted_position_x = position.x = max(0, min(position.x, self.width - 1))

        return Position(adjusted_position_y, adjusted_position_x)

    def get_element(self, position):
        return self.matrix[position.y][position.x]
