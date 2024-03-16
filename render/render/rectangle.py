import pygame.draw

from render.render.renderable import Renderable


class RectRenderable(Renderable):
    def __init__(self, rect, color, border):
        self.x = rect.x
        self.y = rect.y
        self.rect = rect
        self.color = color
        self.border = border

    def render(self, display):
        pygame.draw.rect(display, self.color, self.rect, border_radius=self.border)

    def state(self):
        return f"{self.rect.x}-{self.rect.y}-{self.w}-{self.h}-{self.color}-{self.border}"