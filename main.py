import sys

import pygame

from game.game import Game
from game.menu import Menu
from game.track import Track
from render.renderer import Renderer

pygame.init()
screen = pygame.display.set_mode((900, 600))
renderer = Renderer()

clock = pygame.time.Clock()
game = Game(renderer)
menu = Menu(renderer, game)

boards = [
    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[0, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]],

    [[1, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0]],

    [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]],


]
times = [0, 0.5, 1, 1.5]
game.track = Track(boards, times, 2)

inMenu = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    dt = clock.get_time()/1000

    renderer.render(screen)
    if inMenu:
        game.tick(dt)

    else:
        menu.tick(pygame.mouse.getPressed()[0], pygame.mouse.get_pos())
    clock.tick()
    pygame.display.update()



pygame.quit()
sys.exit()
