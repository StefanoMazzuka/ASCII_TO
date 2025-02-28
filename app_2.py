import pygame
import time
from constants import *
from level import Level
from position import Position

# Inicializar Pygame
pygame.init()

# Configuración de la fuente para determinar el tamaño exacto del carácter
font = pygame.font.SysFont("consolas", 40)  # Ajusta el tamaño de fuente aquí
TILE_WIDTH, TILE_HEIGHT = font.size("█")

# Configuración de pantalla
WIDTH, HEIGHT = 20 * TILE_WIDTH, 20 * TILE_HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colores de elementos
COLORS = {
    WALL: (50, 50, 50),
    FLOOR: (200, 200, 200),
    EMPTY: (255, 255, 255),
    HEART: (255, 0, 0)
}


def draw_map(level):
    """Dibuja el mapa en la pantalla con Pygame usando caracteres."""
    screen.fill((0, 0, 0))  # Fondo negro

    for y, row in enumerate(level.map.matrix):
        for x, element in enumerate(row):
            rect = pygame.Rect(x * TILE_WIDTH, y * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)

            # Dibujar un fondo para la celda
            pygame.draw.rect(screen, (255, 255, 255), rect)
            # pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Bordes

            # Renderizar el carácter que representa el elemento
            text_surface = font.render(element.skin, True, (0, 0, 0))
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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            level.move_player(RIGHT)
        elif keys[pygame.K_a]:
            level.move_player(LEFT)
        elif keys[pygame.K_w]:
            level.move_player(UP)
        elif keys[pygame.K_s]:
            level.move_player(DOWN)

        # Dibujar y actualizar la pantalla
        draw_map(level)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


def main():
    level = Level()
    level.create_map(width=10, height=10)
    level.add_player(Position(4, 4))
    level.add_enemy(Position(6, 6))
    level.add_item(HEART, Position(2, 3))
    level.add_structure(WALL, Position(5, 5))
    level.add_structure(FLOOR, Position(6, 5), collision=False)

    game_loop(level)


if __name__ == "__main__":
    main()
