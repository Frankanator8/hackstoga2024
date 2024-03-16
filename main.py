import sys

import pygame

from game.game import Game
from render.renderer import Renderer

pygame.init()
screen = pygame.display.set_mode((900, 600))

clock = pygame.time.Clock()
game = Game()

renderer = Renderer()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    renderer.render()
    game.tick(pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0], clock.get_time()/1000)
    pygame.display.update()



pygame.quit()
sys.exit()
