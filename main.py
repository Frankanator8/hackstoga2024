import sys

import pygame

from render.renderer import Renderer

pygame.init()
screen = pygame.display.set_mode((900, 600))

clock = pygame.Clock()

renderer = Renderer()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    renderer.render()
    clock.tick()
    pygame.display.update()



pygame.quit()
sys.exit()
