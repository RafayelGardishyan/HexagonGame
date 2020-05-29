import pygame


class GameLogic:
    def __init__(self):
        self.objects = []

    def add_object(self, n_object):
        self.objects.append(n_object)

    def process_input(self, event):
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONUP:
            self.get_object_at_mouse(pygame.mouse.get_pos()).click()
        return True

    def update(self, dt):
        for n_object in self.objects:
            n_object.update(dt)

    def get_object_at_mouse(self, mousepos):
        for n_object in self.objects:
            if n_object.hovered(mousepos):
                return n_object
