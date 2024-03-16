import loader
import game.justlikeyou
from game.odo import odo
from render.render.image import Image


class Menu:
    def __init__(self, renderer, game):
        self.selected = 0
        self.renderer = renderer
        self.game = game
        self.buttons = [
            Image(100, 370, loader.load_image("assets/e/odo_ado.png", size=(300, 150)), "banner1"),
            Image(500, 370, loader.load_image("assets/e/just_like_you_nf.jpg", size=(300, 150)), "banner2"),
        ]
        self.bigdisplay = Image(0, 10, loader.load_image("assets/midnightmoves.png", size=(480, 240)), "disp")
        self.background = Image(0, 0, loader.load_image("assets/e/titlescreen.png", size=(900, 600)), "menuBackground")
        self.render()
        self.lastMousePress = False
        self.active = True

    def render(self):
        self.renderer.add_renderable(self.background, "menuBackground")
        for but in self.buttons:
            self.renderer.add_renderable(but, but.desc)

        self.renderer.add_renderable(self.bigdisplay, "disp")
        

    def unrender(self):
        for but in self.buttons:
            self.renderer.delete_renderable(but.desc)

        self.renderer.delete_renderable("disp")

    def tick(self, mousePressed, mousePos):
        if mousePressed and not self.lastMousePress:
            if 100 <= mousePos[0] <= 400 and 370 <= mousePos[1] <= 520:
                self.active = False
                self.game.track = odo
                self.unrender()
                self.renderer.delete_renderable("menuBackground")
                self.game.back = Image(0, 0, loader.load_image("assets/e/Cartoon_Forest_BG_01.png", size=(900, 600)), "menuBackground")
                self.game.render()

            if 500 <= mousePos[0] <= 800 and 370 <= mousePos[1] <= 520:
                self.active = False
                self.game.track = game.justlikeyou.getTrack()
                self.unrender()
                self.game.song = "justlikeyou.mp3"
                self.renderer.delete_renderable("menuBackground")
                self.game.back = Image(0, 0, loader.load_image("assets/e/Cartoon_Forest_BG_01.png", size=(900, 600)), "menuBackground")
                self.renderer.add_renderable(self.background, "menuBackground")
                self.game.render()
                


        self.lastMousePress = mousePressed

    def tick_passive(self):
        if self.game.track.done:
            if self.game.time > self.game.track.maxLength + 3:
                self.game.unrender()
                self.game.track.reset()
                self.game.track = None
                self.render()
                self.active = True
                self.game.time = 0
