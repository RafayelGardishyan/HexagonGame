from random import randint

import pygame

from game import Renderer
from game.objects.drawable import Drawable


class Grass(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = pygame.image.load(Renderer.asset_path + "/grass.png")
        self.texture.convert()
        self.texture = pygame.transform.rotozoom(self.texture, 0, .02)

        self.lifetime = randint(0, 2)

        self.obj_type = "GRASS"

    def update(self, dt):
        self.lifetime += 1 * dt

    def draw(self, screen: pygame.Surface):
        screen.blit(self.texture, (self.x + Renderer.camera.x_offset, self.y + Renderer.camera.y_offset))

    def grown(self):
        self.lifetime = 0

    def destruct(self):
        self.texture = None