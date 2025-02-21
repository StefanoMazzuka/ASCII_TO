class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[None for _ in range(width)] for _ in range(height)]

    def size(self):
        return self.width, self.height

    def print_top(self):
        print("┏" + "━━━━┳" * (self.width - 1) + "━━━━┓")

    def print_separator(self):
        print("┣" + "━━━━╋" * (self.width - 1) + "━━━━┫")

    def print_bottom(self):
        print("┗" + "━━━━┻" * (self.width - 1) + "━━━━┛")

    def show(self):
        # self.print_top()█◘░▒▓█
        for i, row in enumerate(self.matrix):
            print("┃" + "┃".join(str(tile) if tile is not None else "    " for tile in row) + "┃")
            if i != len(self.matrix) - 1:
                self.print_separator()
        self.print_bottom()