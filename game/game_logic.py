import pygame


class GameLogic:
    def __init__(self):
        self.tiles = []

    def add_tile(self, tile):
        self.tiles.append(tile)

    def process_input(self, event, dt):
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                try:
                    self.get_object_at_mouse(pygame.mouse.get_pos()).click()
                except AttributeError:
                    pass

        return True

    def process_movement(self, keys, camera, dt):

        movement_speed = 50

        if keys[pygame.K_w]:
            camera.move_camera(0, -movement_speed * dt)
        if keys[pygame.K_a]:
            camera.move_camera(-movement_speed * dt, 0)
        if keys[pygame.K_s]:
            camera.move_camera(0, movement_speed * dt)
        if keys[pygame.K_d]:
            camera.move_camera(movement_speed * dt, 0)

    def update(self, dt):
        for tile in self.tiles:
            for entity in tile.entities:
                entity.update(dt)
            tile.update(dt)

    def get_object_at_mouse(self, mousepos):
        for tile in self.tiles:
            for entity in tile.entities:
                if entity.on_me(mousepos):
                    return entity
            if tile.on_me(mousepos):
                return tile

        return None
