from render.render.renderable import Renderable


class Image(Renderable):
    def __init__(self, x, y, image, desc):
        super().__init__(x, y)
        self.image = image
        self.desc = desc

    def render(self, display):
        display.blit(self.image, (self.x, self.y))

    def state(self):
        return f"{self.desc}-({self.x}, {self.y})"