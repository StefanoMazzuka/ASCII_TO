import pygame
import time
from constants import *
from level import Level
from position import Position

# Inicializar Pygame
pygame.init()

# Configuración de la fuente para determinar el tamaño exacto del carácter
# font = pygame.font.SysFont("Cascadia Mono", 40)  # Ajusta el tamaño de fuente aquí
font = pygame.font.Font("resources/font/PressStart2P-Regular.ttf", 20)
TILE_WIDTH, TILE_HEIGHT = font.size("P")
print(f"Tamaño de tile: {TILE_WIDTH}x{TILE_HEIGHT}")

# Configuración de pantalla
WIDTH, HEIGHT = 20 * TILE_WIDTH, 20 * TILE_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def draw_map(map):
    """Dibuja el mapa en la pantalla usando caracteres."""
    screen.fill((0, 0, 0))  # Black background

    map_width_in_px  = map.width * TILE_WIDTH
    map_height_in_px = map.height * TILE_HEIGHT

    # Calculate offsets to center the map
    offset_x = (WIDTH - map_width_in_px) // 2
    offset_y = (HEIGHT - map_height_in_px) // 2

    for y, row in enumerate(map.matrix):
        for x, element in enumerate(row):
            rect = pygame.Rect(
                offset_x + x * TILE_WIDTH,
                offset_y + y * TILE_HEIGHT,
                TILE_WIDTH,
                TILE_HEIGHT
            )

            # Creates a rectangle for each element
            pygame.draw.rect(screen, (255, 255, 255), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Bordes

            # Render the character for the element
            text_surface = font.render(element.skin, True, COLORS.get(element.skin, (0, 0, 0)))
            text_rect = text_surface.get_rect(center=rect.center)
            screen.blit(text_surface, text_rect)


def game_loop(level):
    running = True
    frame_duration = 1 / 10
    enemy_velocity = 1
    player_velocity = 0.25
    enemy_start_time = time.time()
    player_start_time = time.time()

    while running:
        current_time = time.time()

        # Mover enemigos
        if current_time - enemy_start_time >= enemy_velocity:
            level.move_enemies()
            enemy_start_time = current_time

        # Capturar eventos de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mover jugador
        keys = pygame.key.get_pressed()
        for direction in [RIGHT, LEFT, UP, DOWN]:
            if keys[direction]:
                level.move_player(direction)
                break

        # Dibujar y actualizar la pantalla
        draw_map(level.map)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


def main():
    level = Level()
    level.create_map(width=10, height=10)
    level.add_player(Position(4, 4))
    level.add_enemy(Position(6, 6))
    level.add_item(HEART, Position(2, 3))
    level.add_item(DIAMOND, Position(2, 4))
    level.add_item(DIAMOND, Position(2, 11))
    level.add_structure(WALL, Position(5, 5))
    level.add_structure(FLOOR, Position(6, 5), collision=False)

    # print(level.map.matrix[2][11].skin)
    # print(level.map.matrix[2][11].collision)
    # print(level.map.matrix[2][11].pickable)

    game_loop(level)


if __name__ == "__main__":
    main()
