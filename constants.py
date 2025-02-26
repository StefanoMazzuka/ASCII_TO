# BUTTONS
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

BUTTONS = [UP, DOWN, LEFT, RIGHT, EXIT, ITEM_1, ITEM_2, ITEM_3, ITEM_4, ITEM_5]

# CHARACTERS
EMPTY  = ' '
WALL   = '█'
FLOOR  = '░'
DOOR   = 'D'
STAR   = '★'
HEART  = '♥'

# NUMBERS
NUM_ITEMS = 5

# DIRECTIONS
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# PLAYER_MOVEMENTS
PLAYER_MOVEMENTS = {
    UP:    DIRECTIONS[0],
    DOWN:  DIRECTIONS[1],
    LEFT:  DIRECTIONS[2],
    RIGHT: DIRECTIONS[3]
}

# SPRITES
# ҉҈◌▸▾◂☺☼
PLAYER_SPRITES = {
    UP:    '|',
    DOWN:  '|',
    LEFT:  'q',
    RIGHT: 'p'
}
ENEMY_SPRITES = {
    DIRECTIONS[0]: '▴',
    DIRECTIONS[1]: '▾',
    DIRECTIONS[2]: '◂',
    DIRECTIONS[3]: '▸'
}

# ENTITY TYPES
ENEMY = 0
NPC = 1

# ITEMS
ITEMS = {
    ITEM_1: 0,
    ITEM_2: 1,
    ITEM_3: 2,
    ITEM_4: 3,
    ITEM_5: 4
}