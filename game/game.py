import pygame

import loader
from render.render.image import Image
from render.render.rectangle import RectRenderable
from render.render.text import Text
from render.render.textrenderable import TextRenderable


class Game:
    def __init__(self, renderer):
        self.renderBoard = []
        self.renderProgs = []
        for r in range(4):
            self.renderBoard.append([])
            self.renderProgs.append([])
            for c in range(4):
                self.renderBoard[-1].append(RectRenderable(pygame.Rect(40+130*r, 40+130*c, 130, 130), (255, 255, 255), 10, width=1))
                self.renderProgs[-1].append(Image(40+130*r, 40+130*c, loader.load_image("assets/e/IndustrialTile_68.png", size=(130, 130)), f"{r}-{c}"))

        self.playerImg = Image(105-20, 105+25, loader.load_image("assets/banner.jpg", size=(40, 40)), "player")
        self.scoreText = TextRenderable(Text("Score\n0", ("Calibri", 50), (255, 255, 255), (625, 100)))
        self.back = None
        self.playerR = 0
        self.playerC = 0
        self.score = 0
        self.track = None
        self.renderer = renderer
        self.time = 0
        self.song = ""
        self.lastDay = True
        
        


    def render(self):
        self.renderer.add_renderable(self.back, "gameback")
        self.renderer.add_renderable(self.scoreText, "scoreText")
        for r in range(4):
            for c in range(4):
                self.renderer.add_renderable(self.renderBoard[r][c], f"board-{r}-{c}")
                self.renderer.add_renderable(self.renderProgs[r][c], f"prog-{r}-{c}")


        pygame.mixer.music.load("assets/" + self.song)
        pygame.mixer.music.play()

    def unrender(self):
        for r in range(4):
            for c in range(4):
                self.renderer.delete_renderable(f"board-{r}-{c}")
                self.renderer.delete_renderable(f"prog-{r}-{c}")

        self.renderer.delete_renderable("player")
        self.renderer.delete_renderable("gameback")
        self.renderer.delete_renderable("scoreText")

    def tick(self, dt):
        self.time += dt
        if self.track is not None:

            board, nothit = self.track.tick(dt, self.playerR, self.playerC)
            for r, row in enumerate(board):
                for c, col in enumerate(row):
                    self.renderProgs[r][c].x = 40+130*c+65-65*col
                    self.renderProgs[r][c].y = 40+130*r+65-65*col
                    if self.track.switched:
                        self.renderProgs[r][c].image = loader.load_image("assets/e/IndustrialTile_68.png", size=(130*col, 130*col))

                    else:
                        self.renderProgs[r][c].image = loader.load_image("assets/e/Tile_18.png", size=(130*col, 130*col))


        
        #self.renderProgs[r][c].rect = pygame.Rect(105+130*r-65*col, 105+130*c-65*col, 130*col, 130*col)

            if nothit:
                self.score += 1000 * dt

            else:
                self.score -= 3000 * dt


            if self.track.switched:
                self.back.image = loader.load_image("assets/e/Cartoon_Forest_BG_02.png")

            else:
                self.back.image = loader.load_image("assets/e/Cartoon_Forest_BG_01.png")

            self.scoreText.text.set_text(f"Score\n{round(self.score)}")


        else:
            self.time = 0
            self.lastDay = True




