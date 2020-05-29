from math import pi, cos, sin
from random import randint

import pygame
from .drawable import Drawable


class Hexagon(Drawable):
    def __init__(self, x, y, rad, color=(255, 0, 0)):
        super().__init__(x, y, color)
        self.rad = rad

    def draw(self, screen):
        pygame.draw.polygon(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), [
            (self.x + self.rad *
             (cos(2 * pi / 6 * i + self.rotation)),
             self.y + self.rad *
             (sin(2 * pi / 6 * i + self.rotation)))
            for i in range(6)
        ])

    @staticmethod
    def create_grid(w, h, rad, logic):
        for j in range(w):
            x = (j * rad * 2) * (3/4)
            y = ((j * rad * 2) * (1/2)) % (rad * 2)
            for i in range(h):
                logic.objects.append(Hexagon(x, y + i * rad * 2, rad))

    def update(self, dt):
        pass
