from cmath import pi


class Drawable:

    def __init__(self, x, y, color=(0, 255, 0), sec_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
        self.secondary_color = sec_color
        self.texture = None
        self.rotation = 0

    def update(self, dt):
        pass

    def draw(self, screen):
        pass

    def set_color(self, color):
        self.color = color

    def set_texture(self, texture):
        self.texture = texture

    def set_rotation(self, rotation):
        self.rotation = rotation

    def move(self, x_offset, y_offset):
        self.x += x_offset
        self.y += y_offset

    def click(self):
        pass

    def on_me(self, mousepos):
        pass