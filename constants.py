# BUTTONS
from movement import Movement

UP     = 'w'
DOWN   = 's'
LEFT   = 'a'
RIGHT  = 'd'
EXIT   = 'esc'
ITEM_1 = '1'
ITEM_2 = '2'
ITEM_3 = '3'
ITEM_4 = '4'
ITEM_5 = '5'

# CHARACTERS
PLAYER = 'p'
EMPTY  = ' '
WALL   = '█'
FLOOR  = '░'
DOOR   = 'D'
STAR   = '★'
HEART  = '♥'

# NUMBERS
NUM_ITEMS = 5

# MOVEMENTS
MOVEMENTS = {
    UP: Movement.UP,
    DOWN: Movement.DOWN,
    LEFT: Movement.LEFT,
    RIGHT: Movement.RIGHT
}
SPRITES = {
    UP: '|',
    DOWN: '|',
    LEFT: 'q',
    RIGHT: 'p'
}

# ITEMS
ITEMS = {
    ITEM_1: 0,
    ITEM_2: 1,
    ITEM_3: 2,
    ITEM_4: 3,
    ITEM_5: 4
}