from constants import EMPTY
from position import Position
from element import Element


class Map:
    def __init__(self, width: int, height: int):
        self.width  = width
        self.height = height
        self.matrix = [[Element(Position(y, x), EMPTY) for x in range(width)] for y in range(height)]

        self.center_position = Position(int(height / 2), int(width / 2))

    def add_element(self, element: Element, position: Position):
        """Insert an element in the map and return the position."""
        self.matrix[position.y][position.x] = element

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    def _print_top(self):
        return "┏" + "━" * self.width + "┓"

    def _print_bottom(self):
        return "┗" + "━" * self.width + "┛"

    def __str__(self):
        """Print the map."""
        result = self._print_top()
        for row in self.matrix:
            result += "┃" + "".join(element.skin for element in row) + "┃" + "\n"
        result += self._print_bottom()

        return result

    def out_of_bounds(self, position: Position) -> bool:
        """Check if the position is out of bounds."""
        return not (0 <= position.y < self.height and 0 <= position.x < self.width)

    def adjust_position_within_bounds(self, position: Position) -> Position:
        """Adjust the position to be within the bounds of the map."""
        if position is None:
            position = self.center_position

        adjusted_position_y = position.y = max(0, min(position.y, self.height - 1))
        adjusted_position_x = position.x = max(0, min(position.x, self.width - 1))

        return Position(adjusted_position_y, adjusted_position_x)

    def get_element(self, position: Position) -> Element:
        return self.matrix[position.y][position.x]
