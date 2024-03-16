import pygame

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
                renderer.add_renderable(self.renderBoard[-1][-1], f"board-{r}-{c}")
                renderer.add_renderable(self.renderProgs[-1][-1], f"prog-{r}-{c}")

        self.playerR = 0
        self.playerC = 0
        self.score = 0
        self.track = None

    def tick(self, dt):
        if self.track is not None:
            board, nothit = self.track.tick(dt, self.playerR, self.playerC)
            for r, row in enumerate(board):
                for c, col in enumerate(row):
                    self.renderProgs[r][c].rect = pygame.Rect(105+130*r-65*col, 105+130*c-65*col, 130*col, 130*col)

            if nothit:
                self.score += 1000 * dt

            else:
                self.score -= 3000 * dt




