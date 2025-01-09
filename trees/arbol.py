import pygame
import math
from random import randint

# Inicializa PyGame
pygame.init()

# Dimensiones de la pantalla
width, height = 600, 600
screen = pygame.display.set_mode((width, height))

# Título de la ventana
pygame.display.set_caption('Árbol Fractal')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Ángulo de inclinación de las ramas
angle = math.pi / 6  # 30 grados

# Función recursiva para dibujar el árbol fractal
def draw_tree(x, y, length, angle, depth):
    if depth > 0:
        # Calcular la posición de la punta de la rama
        x_end = x + length * math.cos(angle) 
        y_end = y + length * math.sin(angle)

        # Dibujar la rama
        
        pygame.draw.line(screen, white, (x, y), (x_end, y_end), depth)

        # Recursión para las ramas izquierda y derecha
        draw_tree(x_end, y_end, length * 0.7, angle - math.pi / 6, depth -1)  # Rama izquierda
        draw_tree(x_end, y_end, length * 0.7, angle + math.pi / 6, depth -1)  # Rama derecha

# Función para iniciar el dibujo del árbol
def draw_fractal_tree():
    # Punto inicial en la base del árbol
    start_x = width // 2
    start_y = height

    # Longitud inicial del tronco y profundidad de recursión
    trunk_length = 150
    depth = 10  # Número de niveles de recursión

    # Dibujar el tronco y las ramas
    draw_tree(start_x, start_y, trunk_length, -math.pi / 2, depth)

# Bucle principal
running = True
screen.fill(black)  # Fondo negro
draw_fractal_tree()  # Dibujar el árbol fractal
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Salir de PyGame
pygame.quit()
