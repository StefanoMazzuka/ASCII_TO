import pygame
from level import Level
from position import Position
from constants import *

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 400, 400
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego ASCII con Pygame")

# Fuente para representar los caracteres ASCII
font = pygame.font.Font(None, 40)  # Fuente predeterminada, tamaño 36

# Crear nivel
level = Level()
level.create_map(10, 10)
level.add_player()
level.add_structure(WALL, Position(2, 2))

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Fondo negro

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                level.move_player(UP)
            elif event.key == pygame.K_s:
                level.move_player(DOWN)
            elif event.key == pygame.K_a:
                level.move_player(LEFT)
            elif event.key == pygame.K_d:
                level.move_player(RIGHT)

    # Dibujar el mapa con ASCII
    for y in range(10):
        for x in range(10):
            element = level.map.get_element(Position(y, x))
            char = element.skin  # Usa el carácter ASCII correspondiente

            # Renderizar el carácter con la fuente y dibujarlo en pantalla
            text_surface = font.render(char, True, (255, 255, 255))  # Texto blanco
            screen.blit(text_surface, (x * TILE_SIZE, y * TILE_SIZE))

    # Dibujar jugador
    player = level.player
    player_surface = font.render(player.skin, True, (255, 255, 255))
    screen.blit(player_surface, (player.position.x * TILE_SIZE, player.position.y * TILE_SIZE))

    pygame.display.update()
    clock.tick(60)  # Limita el juego a 30 FPS

pygame.quit()
