from render.render.renderable import Renderable


class TextRenderable(Renderable):
    def __init__(self, text):
        self.text = text

    def render(self, display):
        self.text.render(display)