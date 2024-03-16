import pygame

class Renderable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, display):
        pass

    def state(self):
        pass
