class Renderer:
    def __init__(self):
        self.renderables = {}

    def add_renderable(self, renderable, tag):
        self.renderables[tag] = renderable

    def delete_renderable(self, tag):
        del self.renderables[tag]

    def render(self, display):
        for renderable in self.renderables.values():
            renderable.render(display)

