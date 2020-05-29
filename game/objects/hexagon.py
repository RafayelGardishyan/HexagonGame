from math import pi, cos, sin, sqrt
from random import choice

import pygame
from .drawable import Drawable
from ..renderer import Renderer


class Hexagon(Drawable):

    types = {
        "WATER": (0, 0, 255),
        "GRASSLAND": (0, 255, 0),
        "DESERT": (255, 255, 100),
        "DIRT": (50, 50, 0)
    }

    def __init__(self, x, y, rad, color=(0, 100, 0)):
        super().__init__(x, y, color)
        self.rad = rad
        self.type = choice(list(self.types.keys()))
        self.color = self.types[self.type]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [
            ((self.x + Renderer.camera.x_offset) + self.rad *
             (cos(2 * pi / 6 * i + self.rotation)),
             (self.y + Renderer.camera.y_offset) + self.rad *
             (sin(2 * pi / 6 * i + self.rotation)))
            for i in range(6)
        ])

        pygame.draw.polygon(screen, self.secondary_color, [
            ((self.x + Renderer.camera.x_offset) + self.rad *
             (cos(2 * pi / 6 * i + self.rotation)),
             (self.y + Renderer.camera.y_offset) + self.rad *
             (sin(2 * pi / 6 * i + self.rotation)))
            for i in range(6)
        ], 1)

    @staticmethod
    def create_grid(w, h, rad, logic):
        for j in range(w):
            x = (j * (rad * 2)) * (3/4)
            y = j * rad % (rad * 2)
            if j % 2 == 1:
                y -= 4

            for i in range(h):
                logic.tiles.append(Hexagon(x, y + i * (sqrt(3) * rad), rad))

    def update(self, dt):
        pass

    def click(self):
        self.type = self.next_type()
        self.color = self.types[self.type]

    def on_me(self, mousepos):
        mousepos = mousepos[0] - Renderer.camera.x_offset, mousepos[1] - Renderer.camera.y_offset
        if (self.x - self.rad) < mousepos[0] < (self.x + self.rad):
            if (self.y - self.rad) < mousepos[1] < (self.y + self.rad):
                return True
        return False

    def next_type(self):
        keyList=sorted(self.types.keys())
        for i, v in enumerate(keyList):
            if v == self.type:
                return keyList[(i + 1) % len(keyList)]
