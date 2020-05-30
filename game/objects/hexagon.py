from math import pi, cos, sin, sqrt
from random import choice, randint

import pygame
from .drawable import Drawable
from .tile_objects.grass import Grass
from ..renderer import Renderer


class Hexagon(Drawable):
    types = {
        "WATER": (0, 0, 255),
        "GRASSLAND": (0, 255, 0),
        "SAND": (255, 255, 100),
        "DIRT": (50, 50, 0)
    }

    def __init__(self, x, y, rad, color=(0, 100, 0)):
        super().__init__(x, y, color)

        self.entities = []
        self.lifetime = 0

        self.rad = rad
        self.type = choice(list(self.types.keys()))
        self.color = self.types[self.type]

        # self.generate_entities()
        self.obj_type = "TILE"

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
        ], 5)

    @staticmethod
    def create_grid(w, h, rad, logic):
        for j in range(w):
            x = (j * (rad * 2)) * (3 / 4)
            y = j * rad % (rad * 2)
            if j % 2 == 1:
                y -= 4

            for i in range(h):
                logic.tiles.append(Hexagon(x, y + i * (sqrt(3) * rad), rad))

    def update(self, dt):
        self.lifetime += 1 * dt
        if self.type == "DIRT" \
                and randint(0, 20) > 19 \
                and int(self.lifetime) % randint(8, 12) == 0:
            self.dirt_update()

        if self.type == "GRASSLAND":
            self.grassland_update()

        if self.type == "WATER":
            self.water_update()

    def click(self):
        self.type = self.next_type()
        self.handle_type_change()

        # Renderer.camera.x_offset = 400 - self.x
        # Renderer.camera.y_offset = 300 - self.y

    def on_me(self, mousepos):
        mousepos = mousepos[0] - Renderer.camera.x_offset, mousepos[1] - Renderer.camera.y_offset
        bounds = self.calculate_boundaries()
        if bounds["horizontal"][0] < mousepos[0] < bounds["horizontal"][1]:
            if bounds["vertical"][0] < mousepos[1] < bounds["vertical"][1]:
                return True
        return False

    def calculate_boundaries(self):
        return {
            "horizontal": (int(self.x - (self.rad * .5)), int(self.x + (self.rad * .5))),
            "vertical": (int(self.y - (self.rad * .5)), int(self.y + (self.rad * .5)))
        }

    def next_type(self):
        keyList = sorted(self.types.keys())
        for i, v in enumerate(keyList):
            if v == self.type:
                return keyList[(i + 1) % len(keyList)]

    def generate_entities(self):
        bounds = self.calculate_boundaries()
        if self.type == "GRASSLAND":
            for i in range(randint(0, 20)):
                self.entities.append(
                    Grass(
                        randint(bounds["horizontal"][0], bounds["horizontal"][1]),
                        randint(bounds["vertical"][0], bounds["vertical"][1]),
                    )
                )

    def dirt_update(self):
        bounds = self.calculate_boundaries()
        self.entities.append(
            Grass(
                randint(bounds["horizontal"][0], bounds["horizontal"][1]),
                randint(bounds["vertical"][0], bounds["vertical"][1]),
            )
        )

        grass_count = 0

        for entity in self.entities:
            if entity.obj_type == "GRASS":
                grass_count += 1

        if grass_count > 5:
            self.type = "GRASSLAND"
            self.handle_type_change()
            self.lifetime = 0
            for entity in self.entities:
                if entity.obj_type is "GRASS":
                    entity.grown()

    def handle_type_change(self):
        self.color = self.types[self.type]

        if self.type == "WATER":
            self.entities = []

    def grassland_update(self):
        i = 0
        while i < len(self.entities):
            try:
                entity = self.entities[i]
            except IndexError:
                continue

            if entity.obj_type == "GRASS":
                if entity.lifetime >= randint(16, 20):
                    self.entities.pop(self.entities.index(entity))
                    entity.destruct()
                else:
                    i += 1

    def water_update(self):
        if self.lifetime > randint(15, 30):
            self.type = "SAND"
            self.handle_type_change()