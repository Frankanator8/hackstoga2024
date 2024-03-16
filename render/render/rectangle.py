import pygame.draw

from render.render.renderable import Renderable


class RectRenderable(Renderable):
    def __init__(self, rect, color, border, width=0):
        self.x = rect.x
        self.y = rect.y
        self.rect = rect
        self.color = color
        self.border = border
        self.width = width

    def render(self, display):
        pygame.draw.rect(display, self.color, self.rect, width=self.width, border_radius=self.border)

    def state(self):
        return f"{self.rect.x}-{self.rect.y}-{self.w}-{self.h}-{self.color}-{self.border}"