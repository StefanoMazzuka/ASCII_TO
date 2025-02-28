from constants import EMPTY
from position import Position
from element import Element


class Map:
    def __init__(self, width: int, height: int):
        self.width  = width + 2
        self.height = height + 2
        self.matrix = [[Element(Position(y, x), EMPTY) for x in range(self.width)] for y in range(self.height)]

        self.center_position = Position(int(self.height / 2), int(self.width / 2))

        self.create_bounds()

    def add_element(self, element: Element, position: Position):
        """Insert an element in the map and return the position."""
        self.matrix[position.y][position.x] = element

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height

    # def _print_top(self):
    #     return "┏" + "━" * self.width + "┓" + "\n"
    #
    # def _print_bottom(self):
    #     return "┗" + "━" * self.width + "┛" + "\n"
    #
    # def __str__(self):
    #     """Print the map."""
    #     result = self._print_top()
    #     for row in self.matrix:
    #         result += "┃" + "".join(element.skin for element in row) + "┃" + "\n"
    #     result += self._print_bottom()
    #
    #     return result

    def create_bounds(self):
        """Create bounds for the map."""
        self.matrix[0][0]                            = Element(Position(0, 0), "┏")
        self.matrix[0][self.width - 1]               = Element(Position(0, self.width - 1), "┓")
        self.matrix[self.height - 1][0]              = Element(Position(self.height - 1, 0), "┗")
        self.matrix[self.height - 1][self.width - 1] = Element(Position(self.height - 1, self.width - 1), "┛")

        for y in range(1, self.height - 1):
            self.matrix[y][0] = Element(Position(y, 0), "┃", collision=True)
            self.matrix[y][self.width - 1] = Element(Position(y, self.width - 1), "┃", collision=True)

        for x in range(1, self.width - 1):
            self.matrix[0][x] = Element(Position(0, x), "━", collision=True)
            self.matrix[self.height - 1][x] = Element(Position(self.height - 1, x), "━", collision=True)

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
