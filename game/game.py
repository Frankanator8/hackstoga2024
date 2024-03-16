import pygame

import loader
from render.render.image import Image
from render.render.rectangle import RectRenderable

class Game:
    def __init__(self, renderer):
        self.renderBoard = []
        self.renderProgs = []
        for r in range(4):
            self.renderBoard.append([])
            self.renderProgs.append([])
            for c in range(4):
                self.renderBoard[-1].append(RectRenderable(pygame.Rect(40+130*r, 40+130*c, 130, 130), (255, 255, 255), 10, width=1))
                self.renderProgs[-1].append(RectRenderable(pygame.Rect(40+130*r, 40+130*c, 130, 130), (255, 0, 0), 10))

        self.playerImg = Image(105-20, 105+25, loader.load_image("assets/banner.jpg", size=(40, 40)), "player")
        self.playerR = 0
        self.playerC = 0
        self.score = 0
        self.track = None
        self.renderer = renderer
        self.time = 0

    def render(self):
        for r in range(4):
            for c in range(4):
                self.renderer.add_renderable(self.renderBoard[r][c], f"board-{r}-{c}")
                self.renderer.add_renderable(self.renderProgs[r][c], f"prog-{r}-{c}")

        self.renderer.add_renderable(self.playerImg, "player")

    def unrender(self):
        for r in range(4):
            for c in range(4):
                self.renderer.delete_renderable(f"board-{r}-{c}")
                self.renderer.delete_renderable(f"prog-{r}-{c}")

        self.renderer.delete_renderable("player")

    def tick(self, dt):
        self.time += dt
        if self.track is not None:
            board, nothit = self.track.tick(dt, self.playerR, self.playerC)
            for r, row in enumerate(board):
                for c, col in enumerate(row):
                    self.renderProgs[r][c].rect = pygame.Rect(105+130*r-65*col, 105+130*c-65*col, 130*col, 130*col)

            if nothit:
                self.score += 1000 * dt

            else:
                self.score -= 3000 * dt


        else:
            self.time = 0




