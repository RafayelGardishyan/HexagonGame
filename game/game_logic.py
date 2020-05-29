import pygame


class GameLogic:
    def __init__(self):
        self.tiles = []

    def add_object(self, tile):
        self.tiles.append(tile)

    def process_input(self, event, dt):
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.get_object_at_mouse(pygame.mouse.get_pos()).click()

        return True

    def process_movement(self, keys, camera, dt):

        movement_speed = 30

        if pygame.key.get_pressed()[pygame.K_UP]:
                camera.move_camera(0, -movement_speed * dt)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
                camera.move_camera(-movement_speed * dt, 0)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
                camera.move_camera(0, movement_speed * dt)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
                camera.move_camera(movement_speed * dt, 0)

    def update(self, dt):
        for n_object in self.tiles:
            n_object.update(dt)

    def get_object_at_mouse(self, mousepos):
        for tile in self.tiles:
            if tile.on_me(mousepos):
                return tile
